# OpenTelemetry Support
---

{NOTE: }

* [OpenTelemetry](https://opentelemetry.io) is an open-source observability framework that provides a set of APIs, SDKs, and tools 
  for collecting, processing, and exporting telemetry data (metrics, traces, and logs) from applications and systems.

* By standardizing data collection and integration, OpenTelemetry enables seamless monitoring and troubleshooting 
  across various platforms and backends, assisting in the analysis of software performance and behavior.

---

* **RavenDB leverages the OpenTelemetry SDK** to send metrics data via the OpenTelemetry Protocol,  
  allowing seamless data collection and analysis by an OpenTelemetry retriever.

* In addition, an OpenTelemetry collector can retrieve data from RavenDB's [Prometheus](../../../server/administration/monitoring/prometheus) endpoint.  
  Learn more [below](../../../server/administration/monitoring/open-telemetry#retrieve-data-from-prometheus).

* OpenTelemetry support is provided for RavenDB instances both on-premises and in the cloud.

---

* In this page:
  * [Enabling OpenTelemetry in RavenDB](../../../server/administration/monitoring/open-telemetry#enabling-opentelemetry-in-ravendb)
  * [RavenDB OpenTelemetry meters](../../../server/administration/monitoring/open-telemetry#ravendb-opentelemetry-meters)
  * [Server identification in metrics](../../../server/administration/monitoring/open-telemetry#server-identification-in-metrics)
  * [The metric instruments](../../../server/administration/monitoring/open-telemetry#the-metric-instruments)
  * [Metrics export options](../../../server/administration/monitoring/open-telemetry#metrics-export-options)
      * [Console](../../../server/administration/monitoring/open-telemetry#console)
      * [OpenTelemetry Protocol](../../../server/administration/monitoring/open-telemetry#opentelemetry-protocol)
  * [Configuring the OpenTelemetry Collector](../../../server/administration/monitoring/open-telemetry#configuring-the-opentelemetry-collector)
      * [Receive data via OLTP ](../../../server/administration/monitoring/open-telemetry#receive-data-via-otlp)
      * [Retrieve data from Prometheus](../../../server/administration/monitoring/open-telemetry#retrieve-data-from-prometheus)

{NOTE/}

---

{PANEL: Enabling OpenTelemetry in RavenDB}

* To enable the OpenTelemetry metrics in RavenDB,  
  you **must** first set the [Monitoring.OpenTelemetry.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.enabled) configuration key to _true_.

* Learn how to customize configuration keys in the [Configuration Overview](../../../server/configuration/configuration-options) article,  
  which outlines all available options.

* Please remember that it is necessary to restart the RavenDB process for changes to take effect.

{PANEL/}

{PANEL: RavenDB OpenTelemetry meters}

Each meter listed below groups similar or related [metric instruments](../../../server/administration/monitoring/open-telemetry#the-metric-instruments).  
Each metric instrument observes some metric value.

Only the most commonly used meters are enabled by default.  
This can be customized through the specified configuration keys.  

RavenDB exposes the following meters:

* **ravendb.server.cpucredits**  
  Description: Exposes status of CPU credits (cloud)  
  Enabled by default: _false_  
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.CPUCredits.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.cpucredits.enabled)  
* **ravendb.server.gc**  
  Description: Exposes detailed information about the Garbage Collector  
  Enabled by default: _false_   
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.GC.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.gc.enabled)  
* **ravendb.server.general**  
  Description: Exposes general info about the cluster and its licensing  
  Enabled by default: _true_  
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.General.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.general.enabled)  
* **ravendb.server.requests**  
  Description: Exposes information about requests processed by server  
  Enabled by default: _true_    
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.Requests.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.requests.enabled)  
* **ravendb.server.resources**  
  Description: Exposes detailed information about resources usage (e.g. CPU etc.)  
  Enabled by default: _true_    
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.Resources.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.resources.enabled)  
* **ravendb.server.storage**  
  Description: Exposes storage information  
  Enabled by default: _true_   
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.Storage.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.storage.enabled)  
* **ravendb.server.totaldatabases**  
  Description: Exposes aggregated information about databases on the server   
  Enabled by default: _true_   
  Configuration key: [Monitoring.OpenTelemetry.Meters.Server.TotalDatabases.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.server.totaldatabases.enabled)  

---

RavenDB also supports exposing meters developed by Microsoft for AspNetCore and .NET Runtime:  

* **Official AspNetCore instrumentation**  
  Description: See the official MS documentation [AspNetCore documentation](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/blob/main/src/OpenTelemetry.Instrumentation.AspNetCore/README.md#metrics)  
  Enabled by default: _false_  
  Configuration key: [Monitoring.OpenTelemetry.Meters.AspNetCore.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.aspnetcore.enabled)  
* **Official Runtime instrumentation**  
  Description: See the official MS documentation [.NET Runtime documentation](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.Runtime#metrics)  
  Enabled by default: _false_   
  Configuration key: [Monitoring.OpenTelemetry.Meters.Runtime.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.meters.runtime.enabled)  

{PANEL/}

{PANEL: Server identification in metrics}

* OpenTelemetry monitoring requires a service instance ID for initialization.  

* The identification of the server that originated each exposed metric will be listed in the `serviceInstanceId` property within the metric data.

* The server instance identification is determined by the following sequence:

    1. **Configuration Key**  
       First, attempt to retrieve the [Monitoring.OpenTelemetry.ServiceInstanceId](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.serviceinstanceid) configuration key.  
    2. **Public URL Hostname**  
       If the configuration key is Not defined, use the server's public URL hostname, provided it is available.
    3. **Node Tag**  
       If the public URL hostname is unavailable, attempt to use the node tag.
    4. **Initialization Failure**  
       If none of the above options are available, OpenTelemetry will Not be initialized.

{PANEL/}

{PANEL: The metric instruments}

#### `ravendb.server.cpucredits`

| Instrument name                                         | Description                               | Instrument type    |
|---------------------------------------------------------|-------------------------------------------|--------------------|
| ravendb.server.cpucredits.alert_raised                  | CPU Credits Any Alert Raised              | Gauge              |
| ravendb.server.cpucredits.background.tasks.alert_raised | CPU Credits Background Tasks Alert Raised | Gauge              |
| ravendb.server.cpucredits.base                          | CPU Credits Base                          | UpDownCounter      |
| ravendb.server.cpucredits.consumption_current           | CPU Credits Gained Per Second             | UpDownCounter      |
| ravendb.server.cpucredits.failover.alert_raised         | CPU Credits Failover Alert Raised         | Gauge              |
| ravendb.server.cpucredits.max                           | CPU Credits Max                           | UpDownCounter      |
| ravendb.server.cpucredits.remaining                     | CPU Credits Remaining                     | Gauge              |

#### `ravendb.server.gc`  

| Instrument name                            | Description                                                                                                         | Instrument type   |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-------------------|
| ravendb.server.gc.compacted                | Specifies if this is a compacting GC or not.                                                                        | Gauge             |
| ravendb.server.gc.concurrent               | Specifies if this is a concurrent GC or not.                                                                        | Gauge             |
| ravendb.server.gc.finalizationpendingcount | Gets the number of objects ready for finalization this GC observed.                                                 | Gauge             |
| ravendb.server.gc.fragmented               | Gets the total fragmentation (in MB) when the last garbage collection occurred.                                     | Gauge             |
| ravendb.server.gc.gclohsize                | Gets the large object heap size (in MB) after the last garbage collection of given kind occurred.                   | Gauge             |
| ravendb.server.gc.generation               | Gets the generation this GC collected.                                                                              | Gauge             |
| ravendb.server.gc.heapsize                 | Gets the total heap size (in MB) when the last garbage collection occurred.                                         | Gauge             |
| ravendb.server.gc.highmemoryloadthreshold  | Gets the high memory load threshold (in MB) when the last garbage collection occurred.                              | Gauge             |
| ravendb.server.gc.index                    | The index of this GC.                                                                                               | Gauge             |
| ravendb.server.gc.memoryload               | Gets the memory load (in MB) when the last garbage collection occurred.                                             | Gauge             |
| ravendb.server.gc.pausedurations1          | Gets the pause durations. First item in the array.                                                                  | Gauge             |
| ravendb.server.gc.pausedurations2          | Gets the pause durations. Second item in the array.                                                                 | Gauge             |
| ravendb.server.gc.pinnedobjectscount       | Gets the number of pinned objects this GC observed.                                                                 | Gauge             |
| ravendb.server.gc.promoted                 | Gets the promoted MB for this GC.                                                                                   | Gauge             |
| ravendb.server.gc.timepercentage           | Gets the pause time percentage in the GC so far.                                                                    | Gauge             |
| ravendb.server.gc.totalavailablememory     | Gets the total available memory (in MB) for the garbage collector to use when the last garbage collection occurred. | Gauge             |
| ravendb.server.gc.totalcommitted           | Gets the total committed MB of the managed heap.                                                                    | Gauge             |

#### `ravendb.server.general`

| Instrument name                                                               | Description                        | Instrument type   |
|-------------------------------------------------------------------------------|------------------------------------|-------------------|
| ravendb.server.general.certificate_server_certificate_expiration_left_seconds | Server certificate expiration left | Gauge             |
| ravendb.server.general.cluster.index                                          | Cluster index                      | UpDownCounter     |
| ravendb.server.general.cluster.node.state                                     | Current node state                 | UpDownCounter     |
| ravendb.server.general.cluster.term                                           | Cluster term                       | UpDownCounter     |
| ravendb.server.general.license.cores.max                                      | Server license max CPU cores       | Gauge             |
| ravendb.server.general.license.cpu.utilized                                   | Server license utilized CPU cores  | Gauge             |
| ravendb.server.general.license.expiration_left_seconds                        | Server license expiration left     | Gauge             |
| ravendb.server.general.license.type                                           | Server license type                | Gauge             |

#### `ravendb.server.resources`

| Instrument name                                                        | Description                                                    | Instrument type |
|------------------------------------------------------------------------|----------------------------------------------------------------|-----------------|
| ravendb.server.resources.available_memory_for_processing               | Available memory for processing \(in MB\)                      | Gauge           |
| ravendb.server.resources.cpu.machine                                   | Machine CPU usage in %                                         | Gauge           |
| ravendb.server.resources.cpu.process                                   | Process CPU usage in %                                         | Gauge           |
| ravendb.server.resources.dirty_memory                                  | Dirty Memory that is used by the scratch buffers in MB         | Gauge           |
| ravendb.server.resources.encryption_buffers.memory_in_pool             | Server encryption buffers memory being in pool in MB           | Gauge           |
| ravendb.server.resources.encryption_buffers.memory_in_use              | Server encryption buffers memory being in use in MB            | Gauge           |
| ravendb.server.resources.io_wait                                       | IO wait in %                                                   | Gauge           |
| ravendb.server.resources.low_memory_flag                               | Server low memory flag value                                   | Gauge           |
| ravendb.server.resources.machine.assigned_processor_count              | Number of assigned processors on the machine                   | UpDownCounter   |
| ravendb.server.resources.machine.processor_count                       | Number of processor on the machine                             | UpDownCounter   |
| ravendb.server.resources.managed_memory                                | Server managed memory size in MB                               | Gauge           |
| ravendb.server.resources.thread_pool.available_completion_port_threads | Number of available completion port threads in the thread pool | Gauge           |
| ravendb.server.resources.thread_pool.available_worker_threads          | Number of available worker threads in the thread pool          | Gauge           |
| ravendb.server.resources.total_memory                                  | Server allocated memory in MB                                  | Gauge           |
| ravendb.server.resources.total.swap_usage                              | Server total swap usage in MB                                  | Gauge           |
| ravendb.server.resources.total.swap.size                               | Server total swap size in MB                                   | Gauge           |
| ravendb.server.resources.unmanaged_memory                              | Server unmanaged memory size in MB                             | Gauge           |
| ravendb.server.resources.working_set_swap_usage                        | Server working set swap usage in MB                            | Gauge           |

#### `ravendb.server.requests`

| Instrument name                                      | Description                                   | Instrument type  |
|------------------------------------------------------|-----------------------------------------------|------------------|
| ravendb.server.requests.requests.average_duration    | Average request time in milliseconds          | Gauge            |
| ravendb.server.requests.requests.concurrent_requests | Number of concurrent requests                 | UpDownCounter    |
| ravendb.server.requests.requests.per_second          | Number of requests per second.                | Gauge            |
| ravendb.server.requests.tcp.active.connections       | Number of active TCP connections              | Gauge            |
| ravendb.server.requests.total.requests               | Total number of requests since server startup | UpDownCounter    |

#### `ravendb.server.storage`

| Instrument name                                                | Description                               | Instrument type   |
|----------------------------------------------------------------|-------------------------------------------|-------------------|
| ravendb.server.storage.storage.disk.ios.read_operations        | IO read operations per second             | Gauge             |
| ravendb.server.storage.storage.disk.ios.write_operations       | IO write operations per second            | Gauge             |
| ravendb.server.storage.storage.disk.queue_length               | Queue length                              | Gauge             |
| ravendb.server.storage.storage.disk.read_throughput            | Read throughput in kilobytes per second   | Gauge             |
| ravendb.server.storage.storage.disk.remaining.space            | Remaining server storage disk space in MB | Gauge             |
| ravendb.server.storage.storage.disk.remaining.space_percentage | Remaining server storage disk space in %  | Gauge             |
| ravendb.server.storage.storage.disk.write_throughput           | Write throughput in kilobytes per second  | Gauge             |
| ravendb.server.storage.storage.total_size                      | Server storage total size in MB           | Gauge             |
| ravendb.server.storage.storage.used_size                       | Server storage used size in MB            | Gauge             |

#### `ravendb.server.totaldatabases`

| Instrument name                                                   | Description                                                                                        | Instrument type   |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------|
| ravendb.server.totaldatabases.count_stale_indexes                 | Number of stale indexes in all loaded databases                                                    | UpDownCounter     |
| ravendb.server.totaldatabases.data.written.per_second             | Number of bytes written \(documents, attachments, counters, timeseries\) in all loaded databases   | Gauge             |
| ravendb.server.totaldatabases.database.disabled_count             | Number of disabled databases                                                                       | UpDownCounter     |
| ravendb.server.totaldatabases.database.encrypted_count            | Number of encrypted databases                                                                      | UpDownCounter     |
| ravendb.server.totaldatabases.database.faulted_count              | Number of faulted databases                                                                        | UpDownCounter     |
| ravendb.server.totaldatabases.database.loaded_count               | Number of loaded databases                                                                         | UpDownCounter     |
| ravendb.server.totaldatabases.database.node_count                 | Number of databases for current node                                                               | UpDownCounter     |
| ravendb.server.totaldatabases.database.total_count                | Number of all databases                                                                            | UpDownCounter     |
| ravendb.server.totaldatabases.map_reduce.index.mapped_per_second  | Number of maps per second for map-reduce indexes \(one minute rate\) in all loaded databases       | Gauge             |
| ravendb.server.totaldatabases.map_reduce.index.reduced_per_second | Number of reduces per second for map-reduce indexes \(one minute rate\) in all loaded databases    | Gauge             |
| ravendb.server.totaldatabases.map.index.indexed_per_second        | Number of indexed documents per second for map indexes \(one minute rate\) in all loaded databases | Gauge             |
| ravendb.server.totaldatabases.number_error_indexes                | Number of error indexes in all loaded databases                                                    | UpDownCounter     |
| ravendb.server.totaldatabases.number_of_indexes                   | Number of indexes in all loaded databases                                                          | UpDownCounter     |
| ravendb.server.totaldatabases.number.faulty_indexes               | Number of faulty indexes in all loaded databases                                                   | UpDownCounter     |
| ravendb.server.totaldatabases.writes_per_second                   | Number of writes \(documents, attachments, counters, timeseries\) in all loaded databases          | Gauge             |

{PANEL/}

{PANEL: Metrics export options}

RavenDB offers two options for exporting metrics:  

  * Export data to the console for immediate metrics insight.
  * Export data via the OpenTelemetry Protocol (OTLP) for integration with other observability platforms.

{NOTE: }

<a id="console" /> __Console__:

---

* RavenDB can output telemetry data directly to the console,  
  providing real-time, local visibility of the OpenTelemetry metrics.  

* This is particularly useful for local development and debugging,  
  as it eliminates the need for integration with external monitoring systems or observability platforms.

* To enable output to the console -  
  set the [Monitoring.OpenTelemetry.ConsoleExporter](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.consoleexporter) configuration key to _true_.

{NOTE/}
{NOTE: }

<a id="opentelemetry-protocol" /> __OpenTelemetry Protocol__:

---

* OpenTelemetry supports the **OpenTelemetry Protocol** (OTLP),  
  a standard wire protocol used by all OpenTelemetry SDKs.

* This protocol allows data to be sent from metrics producers (e.g. RavenDB) to any software that supports OTLP.  
  The recommended software, as suggested by OpenTelemetry, is called **OpenTelemetry Collector**.  
  The Collector can be further configured to forward and export this data to various analysis tools.  
  Learn about the OpenTelemetry Collector on the official documentation site: [OTel Collector](https://opentelemetry.io/docs/collector/).

* RavenDB supports the official OTLP by default, allowing you to export RavenDB metrics to the OpenTelemetry Collector.

* To enable exporting metrics via the OpenTelemetry Protocol -  
  set the [Monitoring.OpenTelemetry.OpenTelemetryProtocol.Enabled](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.enabled) configuration key to _true_.

* By default, RavenDB does not override the OpenTelemetry Protocol exporter default values.  
  However, customization is available via the following configuration options:  

| Configuration key                                                                                                                                                                                   | Description                                                                                                                                                                | Accepted values      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Monitoring.OpenTelemetry.OpenTelemetryProtocol<br>[.ExportProcessorType](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.exportprocessortype) | Export processor type                                                                                                                                                      | Simple / Batch       |
| Monitoring.OpenTelemetry.OpenTelemetryProtocol<br>[.Headers](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.headers)                         | Custom headers                                                                                                                                                             | string               |
| Monitoring.OpenTelemetry.OpenTelemetryProtocol<br>[.Protocol](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.protocol)                       | Defines the transport protocol that OpenTelemetry Protocol should use to send data.                                                                                        | gRPC / HttpProtobuf  |
| Monitoring.OpenTelemetry.OpenTelemetryProtocol<br>[.Endpoint](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.endpoint)                       | Endpoint where OpenTelemetry Protocol should send data.<br>See configuration details [below](../../../server/administration/monitoring/open-telemetry#configure-endpoint). | string               |
| Monitoring.OpenTelemetry.OpenTelemetryProtocol<br>[.Timeout](../../../server/configuration/monitoring-configuration#monitoring.opentelemetry.opentelemetryprotocol.timeout)                         | Timeout                                                                                                                                                                    | int                  |

{NOTE/}

{INFO: }

<a id="configure-endpoint" /> __Configuring the OpenTelemetry Protocol endpoint__:

---
 
The defined endpoint must correspond to the endpoint [configured on the collector](../../../server/administration/monitoring/open-telemetry#configuring-the-opentelemetry-collector) for receiving metrics data.
The endpoint format should match the transport protocol you are using:

<br>

* **HttpProtobuf** protocol:

  * HttpProtobuf is a transport protocol used for efficiently serializing structured data over HTTP  
    using Protocol Buffers (Protobuf).
  
  * The current official .NET implementation adheres to the OpenTelemetry specification,  
    which requires specifying the complete path to the collector endpoint when exporting metrics.  
    By default, the endpoint path for the OpenTelemetry Collector is `/v1/metrics.`
  
  * So, for example, if you are using the default settings for the OpenTelemetry Collector  
    and utilizing **HttpProtobuf** as the transport protocol, the endpoint used would be 
    `http://localhost:4318/v1/metrics` (replace the default port 4318 with whatever port you are using).

* **gRPC** protocol:

  * When using the default settings for the OpenTelemetry Collector with the **gRPC** transport protocol,  
    the endpoint should be specified in the format `grpc://localhost:4317`  
    (replace the default port 4317 with whatever port you are using).
  
  * The gRPC endpoint does not include a path like _/v1/metrics_.

{INFO/}

{PANEL/}

{PANEL: Configuring the OpenTelemetry Collector}

* The OpenTelemetry Collector is a vendor-agnostic proxy that can receive, process, and export telemetry data (traces, metrics, logs)
  from multiple sources to different backends. It acts as a centralized point for collecting and processing telemetry data.

* In the OpenTelemetry Collector configuration, a **receiver** is a component that listens for incoming telemetry data. 

* Configure the receiver to either:  
   * Receive data via OTLP from RavenDB
   * Retrieve data from RavenDB's Prometheus endpoint

{NOTE: }

<a id="receive-data-via-otlp" /> __Receive data via OTLP__:

---

* The `otlp` receiver is used for receiving telemetry data in the OpenTelemetry Protocol (OTLP) format.

* Specify the `endpoints` where the OpenTelemetry Collector should listen for incoming telemetry data,  
  whether via gRPC or HTTP, and on which ports.  
  (4317 is the default port for gRPC, and 4318 is the default port for HTTP protocol).

* For example, define your controller like so:

    {CODE-BLOCK: json}
receivers:
    otlp:
        protocols:
            grpc:
                endpoint: localhost:4317
            http:
                endpoint: localhost:4318
    {CODE-BLOCK/}

{NOTE/}
{NOTE: }
 
<a id="retrieve-data-from-prometheus" /> __Retrieve data from Prometheus__:

---

* The OpenTelemetry Collector includes support for retrieving metrics from a Prometheus endpoint.  

* RavenDB provides a Prometheus endpoint that can be used as a data source for the OpenTelemetry Collector.
  This endpoint provides metrics in a standardized format and integrates seamlessly without requiring you to enable OpenTelemetry in RavenDB.

* Use the `prometheus_simple` receiver in your OpenTelemetry Collector configuration.  
  This setup instructs the collector to scrape metrics from a Prometheus endpoint.

* Specify the address of your RavenDB server in the `endpoint` key.  
  Specify RavenDB's Prometheus endpoint path in the `metrics_path` key.  

* A sample configuration may look like this:  

    {CODE-BLOCK: json}
receivers:
    prometheus_simple:
        endpoint: "http://localhost:8080"  # Replace with your RavenDB instance address
        metrics_path: "/admin/monitoring/v1/prometheus"  # RavenDB's prometheus endpoint path
        collection_interval: 10s
        tls:
            cert_file: "D:\\cert.crt"
            key_file: "D:\\key.key"
            insecure: false
            insecure_skip_verify: false
    {CODE-BLOCK/}

* The configuration above sets up the OpenTelemetry Collector to scrape Prometheus-formatted metrics from a RavenDB server.  
  The collector will access `http://localhost:8080/admin/monitoring/v1/prometheus` to retrieve the metrics.
 
{NOTE/}
{PANEL/}

## Related Articles

### Monitoring

- [Telegraf plugin](../../../server/administration/monitoring/telegraf)
- [Prometheus](../../../server/administration/monitoring/prometheus)

### Configuration

- [Configuration overview](../../../server/configuration/configuration-options)
- [Monitoring configuration](../../../server/configuration/monitoring-configuration)
