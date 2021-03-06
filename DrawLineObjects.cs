using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using SimpleJSON;
using System;

public class DrawLineObjects : MonoBehaviour
{
    public GameObject linePrefab;
    public string fileName;
    public float overrideWidth = 0;
    
    // Start is called before the first frame update
    void Start()
    {
        var importedJson = JSON.Parse(ReadString());
        for (int i=0; i < importedJson["groups"].Count; i++) {
            LineRenderer lr = Instantiate(linePrefab, transform).GetComponent<LineRenderer>();
            if (importedJson["groups"][i]["loop"]) {
                lr.loop = true;
            }
            if (overrideWidth > 0) {
                lr.widthCurve = AnimationCurve.Linear(0, overrideWidth, 1, overrideWidth);
            } else {
                lr.widthCurve = AnimationCurve.Linear(0, importedJson["groups"][i]["width"], 1, importedJson["groups"][i]["width"]);
            }
            int pointCount = importedJson["groups"][i]["points"].Count;
            Vector3[] pointList = new Vector3[pointCount];
            for (int j=0; j < pointCount; j++) {
                pointList[j] = importedJson["groups"][i]["points"][j].ReadVector3();
            }
            lr.positionCount = pointList.Length;
            lr.SetPositions(pointList);
        }
    }

    string ReadString()
    {
        string path = "Assets/LineObjects/"+ fileName +".json";

        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path); 
        string text = reader.ReadToEnd();
        reader.Close();
        return text;
    }
}
