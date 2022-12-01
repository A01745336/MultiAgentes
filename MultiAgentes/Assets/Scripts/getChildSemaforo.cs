using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class getChildSemaforo : MonoBehaviour
{
    public GameObject semaforoRojo;
    public GameObject semaforoVerde;
    void Start(){
        semaforoRojo= this.gameObject.transform.GetChild(0).gameObject;
        semaforoVerde = this.gameObject.transform.GetChild(1).gameObject;
    }
    public void SetSemaforoRojo(){
        semaforoRojo.SetActive(true);
        semaforoVerde.SetActive(false);
    }
    public void SetSemaforoVerde(){
        semaforoRojo.SetActive(false);
        semaforoVerde.SetActive(true);
    }
}
