using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using SimpleJSON;
using System;

// imports drawing line into unity
public class DrawLineObjects : MonoBehaviour
{
    public GameObject linePrefab;
    public bool loop;
    // Start is called before the first frame update
    void Start()
    {
        var importedJson = JSON.Parse(ReadString());
        for (int i=0; i < importedJson["groups"].Count; i++) {
            LineRenderer lr = Instantiate(linePrefab).GetComponent<LineRenderer>();
            int pointCount = importedJson["groups"][i].Count + Convert.ToInt32(loop);
            Vector3[] pointList = new Vector3[pointCount];
            for (int j=0; j < pointCount - Convert.ToInt32(loop); j++) {
                pointList[j] = importedJson["groups"][i][j].ReadVector3();
            }
            if (loop) {
                pointList[pointCount-1] = importedJson["groups"][i][0].ReadVector3();
            }
            lr.positionCount = pointList.Length;
            lr.SetPositions(pointList);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    string ReadString()
    {
        string path = "Assets/Scripts/CylJson.json";

        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path); 
        string text = reader.ReadToEnd();
        reader.Close();
        return text;
    }
}
