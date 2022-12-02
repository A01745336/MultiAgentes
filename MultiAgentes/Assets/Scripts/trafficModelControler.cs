using System;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Networking;


[Serializable]
public class DatosCarros
{
    public string id;
    public float x, y, z;

    public DatosCarros(string id, float x, float y, float z)
    {
        this.id = id;
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

[Serializable]

public class CarroData
{
    public List<DatosCarros> positions;

    public CarroData() => this.positions = new List<DatosCarros>();
}

[Serializable]
public class DatosSemaforos
{
    public string id;
    public float x, y, z;
    public bool semaforoActive;

    public DatosSemaforos(string id, float x, float y, float z, bool semaforoActive)
    {
        this.id = id;
        this.x = x;
        this.y = y;
        this.z = z;
        this.semaforoActive = semaforoActive;
    }
}

[Serializable]

public class SemaforoData
{
    public List<DatosSemaforos> positions;

    public SemaforoData() => this.positions = new List<DatosSemaforos>();
}

public class trafficModelControler : MonoBehaviour
{
    string serverUrl = "http://localhost:8585";
    string getCarroEndpoint = "/getCarro";
    string getSemaforoEndpoint = "/getSemaforo";
    string sendConfigEndpoint = "/init";
    string updateEndpoint = "/update";
    [SerializeField] TextAsset layout;
    [SerializeField] int tileSize;
    public bool crearCiudad;
    CarroData carrosData;
    SemaforoData semaforosData;
    Dictionary<string, GameObject> carros;
    Dictionary<string, GameObject> semaforos;
    Dictionary<string, Vector3> prevPositions, currPositions;

    bool updated = false, started = false, startedSemaforo = false, updatedSemaforo = false;

    public GameObject carroPrefab, luzSemaforoPrefab, semaforo1Prefab, parkingPrefab, roadPrefab, edificioPrefab, pastoPrefab, arbolPrefab, pavimentoPrefab, esquinaPrefab, lamparaPrefab, crucePeatonalPrefab, piso;
    public int numeroCarros = 100;
    public int ancho, alto;
    public float timeToUpdate = 5.0f;
    private float timer, dt;

    void Start()
    {
        if (crearCiudad)
            MakeTiles(layout.text);

        carrosData = new CarroData();
        semaforosData = new SemaforoData();

        prevPositions = new Dictionary<string, Vector3>();
        currPositions = new Dictionary<string, Vector3>();

        carros = new Dictionary<string, GameObject>();
        semaforos = new Dictionary<string, GameObject>();

        piso.transform.localScale = new Vector3((float)(ancho + 1) / 10, 1, (float)(alto + 1) / 10);
        piso.transform.localPosition = new Vector3((float)ancho/2-0.5f, 0, (float)alto/2-0.5f);

        timer = timeToUpdate;

        StartCoroutine(SendConfiguration());
    }

        private void Update()
    {
        if(timer < 0)
        {
            timer = timeToUpdate;
            updated = false;
            StartCoroutine(UpdateSimulation());
        }

        if (updated)
        {
            timer -= Time.deltaTime;
            dt = 1.0f - (timer / timeToUpdate);

            foreach(var carro in currPositions)
            {
                Vector3 currentPosition = carro.Value;
                Vector3 previousPosition = prevPositions[carro.Key];

                Vector3 interpolated = Vector3.Lerp(previousPosition, currentPosition, dt);
                Vector3 direction = currentPosition - interpolated;

                carros[carro.Key].transform.localPosition = interpolated;
                if(direction != Vector3.zero) carros[carro.Key].transform.rotation = Quaternion.LookRotation(direction);
            }
        }
    }

    void MakeTiles(string tiles)
    {
        int x = 0;
        int y = tiles.Split('\n').Length - 2;

        Vector3 position;
        GameObject tile;

        for (int i = 0; i < tiles.Length; i++) {
            if (tiles[i] == '>' || tiles[i] == '<') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.25f, 0.25f, 0.25f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'v' || tiles[i] == '^') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(roadPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.25f, .25f, 0.25f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 's') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(crucePeatonalPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.25f, 0.25f, 0.25f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'S') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(crucePeatonalPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.25f, 0.25f, 0.25f);
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == 'c') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(semaforo1Prefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'C') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(semaforo1Prefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'P') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pastoPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(arbolPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(1, UnityEngine.Random.Range(1.0f, 2.0f), 1);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'D') {
                position = new Vector3(x * tileSize - 0.5f, 0, y * tileSize + 0.2f);
                tile = Instantiate(edificioPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.1f, UnityEngine.Random.Range(0.1f, 0.5f), 0.1f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '#') {
                position = new Vector3(x * tileSize - 0.5f, 0, y * tileSize + 0.2f);
                tile = Instantiate(edificioPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.1f, UnityEngine.Random.Range(0.1f, 0.3f), 0.1f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'A') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.Euler(0, 0, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'a') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.Euler(0, 180, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == 'B') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.Euler(0, 270, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'b') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(pavimentoPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'X') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(esquinaPrefab, position, Quaternion.Euler(0, 180, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(lamparaPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'x') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(esquinaPrefab, position, Quaternion.Euler(0, 270, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(lamparaPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            }else if (tiles[i] == 'Y') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(esquinaPrefab, position, Quaternion.Euler(0, 90, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(lamparaPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.5f, 0.5f, 0.5f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == 'y') {
                position = new Vector3(x * tileSize, 0, y * tileSize);
                tile = Instantiate(esquinaPrefab, position, Quaternion.Euler(0, 0, 0));
                tile.transform.localScale = new Vector3(0.5f, 0.25f, 0.5f);
                tile.transform.parent = transform;
                tile = Instantiate(lamparaPrefab, position, Quaternion.identity);
                tile.transform.localScale = new Vector3(0.25f, 0.25f, 0.25f);
                tile.transform.parent = transform;
                x += 1;
            } else if (tiles[i] == '\n') {
                x = 0;
                y -= 1;
            }
        }
    }

    IEnumerator UpdateSimulation()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + updateEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            StartCoroutine(GetCarrosData());
            StartCoroutine(GetSemaforosData());
        }
    }

    IEnumerator SendConfiguration()
    {
        WWWForm form = new WWWForm();

        form.AddField("numeroCarros", numeroCarros.ToString());
        form.AddField("ancho", ancho.ToString());
        form.AddField("alto", alto.ToString());

        UnityWebRequest www = UnityWebRequest.Post(serverUrl + sendConfigEndpoint, form);
        www.SetRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("Configuration upload complete!");
            Debug.Log("Getting Agents positions");
            StartCoroutine(GetCarrosData());
            StartCoroutine(GetSemaforosData());
        }
    }

    IEnumerator GetCarrosData()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + getCarroEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            carrosData = JsonUtility.FromJson<CarroData>(www.downloadHandler.text);

            foreach(DatosCarros carro in carrosData.positions)
            {
                Vector3 newCarroPosition = new Vector3(carro.x, carro.y, carro.z);

                    if(!started)
                    {
                        prevPositions[carro.id] = newCarroPosition;
                        carros[carro.id] = Instantiate(carroPrefab, newCarroPosition, Quaternion.identity);
                    }
                    else
                    {
                        Vector3 currentPosition = new Vector3();
                        if(currPositions.TryGetValue(carro.id, out currentPosition))
                            prevPositions[carro.id] = currentPosition;
                        currPositions[carro.id] = newCarroPosition;
                    }
            }

            updated = true;
            if(!started) started = true;
        }
    }

    IEnumerator GetSemaforosData()
    {
        UnityWebRequest www = UnityWebRequest.Get(serverUrl + getSemaforoEndpoint);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
            Debug.Log(www.error);
        else
        {
            semaforosData = JsonUtility.FromJson<SemaforoData>(www.downloadHandler.text);

            foreach(DatosSemaforos luzSemaforo in semaforosData.positions)
            {
                if (!startedSemaforo)
                {
                    Vector3 semaforoPos = new Vector3(luzSemaforo.x, luzSemaforo.y, luzSemaforo.z);
                    semaforos[luzSemaforo.id] = Instantiate(luzSemaforoPrefab, new Vector3(luzSemaforo.x, luzSemaforo.y, luzSemaforo.z), Quaternion.identity);
                }
                else
                {
                    if (luzSemaforo.semaforoActive){
                        semaforos[luzSemaforo.id].GetComponent<getChildSemaforo>().SetSemaforoRojo();
                    } else {
                        semaforos[luzSemaforo.id].GetComponent<getChildSemaforo>().SetSemaforoVerde();
                    }
                }
            }

            if (!startedSemaforo) startedSemaforo = true;
        }
    }
}
