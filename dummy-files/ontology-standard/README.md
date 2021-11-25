**Standardized ontology in the context of autonomous driving v1**

The Automotive Standardization Consortium (Austac) defines in the following document the ontology for Digital Twins for Advanced Driver Assistance Systems (ADAS). The presented data structure and sensor types standardizes the use of generated sensor data among various autonomous vehicles.

The Digital Twins Definition Language (DTDL) Version 2 [Azu20] is being used for developing the model of digital twins. The format of the files describing digital twins is called JSON-LD and is based on the JSON format, but with the additional benefit of serializing Linked Data while preserving simplicity and compatibility with JSON [Lan13].

Firstly, the **interface** contains an overview of the content for any digital twin. In it, the Properties and Components are described. For our purpose the vehicle is the first interface linking the sensors interfaces.

| **Property** | **Data type** | **Description** | **Content for v1** |
| --- | --- | --- | --- |
| @id | Digital Twin Model Identifier: \&lt;scheme\&gt;: \&lt;path\&gt;; \&lt;version\&gt; | A digital twin model identifier for the interface | dtmi:taiax:vehicle;1 |
| @type | Internationalized Resource Identifier | This must be &quot;Interface&quot; | Interface |
| @context | Internationalized Resource Identifier | A comment for model authors | dtmi:dtdl:context;2 |
| contents | set of Telemetry, Properties, Commands, Relationships, Components | A set of objects that define the contents (Telemetry, Properties, Commands, Relationships, and/or Components) of this interface | Properties,Components |

The following interface shows a vehicle with the sensor as a component. Inside the component list, the schema links the vehicle with the respective sensor interfaces.
```
{
  "@id": "dtmi:taiax:vehicle;1",
  "@type": "Interface",
  "@context": "dtmi:dtdl:context;2",
  "contents": [
    {
      "@type": "Property",
      "name": "vehicle_name",
      "schema": "string"
    },
    {
      "@type": "Component",
      "name": "Battery_Sensor",
      "schema": "dtmi:taiax:battery;1"
    },
    {
      "@type": "Component",
      "name": "Camera",
      "schema": "dtmi:taiax:camera;1"
    },
    {
      "@type": "Component",
      "name": "GNSS-Sensor",
      "schema": "dtmi:taiax:gnss;1"
    },
    {
      "@type": "Component",
      "name": "IMU-Sensor",
      "schema": "dtmi:taiax:imu;1"
    },
    {
      "@type": "Component",
      "name": "LIDAR",
      "schema": "dtmi:taiax:lidar;1"
    },
    {
      "@type": "Component",
      "name": "Radar",
      "schema": "dtmi:taiax:radar;1"
    },
    {
      "@type": "Component",
      "name": "Semantic_LIDAR",
      "schema": "dtmi:taiax:slidar;1"
    }
  ]
}
```

The following interface shows the structure of a gnss-sensor.

```
{
  "@id": "dtmi:taiax:gnss;1",
  "@type": "Interface",
  "@context": "dtmi:dtdl:context;2",
  "contents": [
    {
      "@type": "Telemetry",
      "name": "gnss",
      "schema": {
        "@type": "Object",
        "fields": [
          {
            "name": "altitude",
            "schema": "float"
          },
          {
            "name": "latitude",
            "schema": "float"
          },
          {
            "name": "longitude",
            "schema": "float"
          }
        ]
      }
    }
  ]
}
```


References

[Azu20] Azure: Digital Twins Definition Language (DTDL). Version 2. https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md, 22.11.2021.

[Lan13] Lanthaler, M.: Creating 3rd Generation Web APIs with Hydra: Proceedings of the 22nd International Conference on World Wide Web. Association for Computing Machinery, New York, NY, USA, 2013; S. 35–38.