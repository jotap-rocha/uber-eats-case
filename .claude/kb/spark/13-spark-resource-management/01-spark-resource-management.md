# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.resource.html#

# Resource Management#

## Core Classes#

[`ResourceInformation`](api/pyspark.resource.ResourceInformation.html#pyspark.resource.ResourceInformation "pyspark.resource.ResourceInformation")(name,Â addresses) | Class to hold information about a type of Resource.  
---|---  
[`ResourceProfile`](api/pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")([_java_resource_profile,Â ...]) | Resource profile to associate with an RDD.  
[`ResourceProfileBuilder`](api/pyspark.resource.ResourceProfileBuilder.html#pyspark.resource.ResourceProfileBuilder "pyspark.resource.ResourceProfileBuilder")() | Resource profile Builder to build a resource profile to associate with an RDD.  
[`ExecutorResourceRequest`](api/pyspark.resource.ExecutorResourceRequest.html#pyspark.resource.ExecutorResourceRequest "pyspark.resource.ExecutorResourceRequest")(resourceName,Â amount) | An Executor resource request.  
[`ExecutorResourceRequests`](api/pyspark.resource.ExecutorResourceRequests.html#pyspark.resource.ExecutorResourceRequests "pyspark.resource.ExecutorResourceRequests")([_jvm,Â _requests]) | A set of Executor resource requests.  
[`TaskResourceRequest`](api/pyspark.resource.TaskResourceRequest.html#pyspark.resource.TaskResourceRequest "pyspark.resource.TaskResourceRequest")(resourceName,Â amount) | A task resource request.  
[`TaskResourceRequests`](api/pyspark.resource.TaskResourceRequests.html#pyspark.resource.TaskResourceRequests "pyspark.resource.TaskResourceRequests")([_jvm,Â _requests]) | A set of task resource requests.  
  
__On this page

[ __Show Source](../_sources/reference/pyspark.resource.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.ResourceInformation.html

# pyspark.resource.ResourceInformation#

_class _pyspark.resource.ResourceInformation(_name_ , _addresses_)[[source]](../../_modules/pyspark/resource/information.html#ResourceInformation)#
    

Class to hold information about a type of Resource. A resource could be a GPU, FPGA, etc. The array of addresses are resource specific and its up to the user to interpret the address.

One example is GPUs, where the addresses would be the indices of the GPUs

New in version 3.0.0.

Parameters
    

**name** str
    

the name of the resource

**addresses** list
    

a list of strings describing the addresses of the resource

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Attributes

`addresses` | 

Returns
      
---|---  
`name` | 

Returns
      
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.ResourceInformation.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.ResourceProfile.html

# pyspark.resource.ResourceProfile#

_class _pyspark.resource.ResourceProfile(__java_resource_profile =None_, __exec_req =None_, __task_req =None_)[[source]](../../_modules/pyspark/resource/profile.html#ResourceProfile)#
    

Resource profile to associate with an RDD. A `pyspark.resource.ResourceProfile` allows the user to specify executor and task requirements for an RDD that will get applied during a stage. This allows the user to change the resource requirements between stages. This is meant to be immutable so user cannot change it after building.

New in version 3.1.0.

Changed in version 4.0.0: Supports Spark Connect.

Notes

This API is evolving.

Examples

Create Executor resource requests.
    
    
    >>> executor_requests = (
    ...     ExecutorResourceRequests()
    ...     .cores(2)
    ...     .memory("6g")
    ...     .memoryOverhead("1g")
    ...     .pysparkMemory("2g")
    ...     .offheapMemory("3g")
    ...     .resource("gpu", 2, "testGpus", "nvidia.com")
    ... )
    

Create task resource requasts.
    
    
    >>> task_requests = TaskResourceRequests().cpus(2).resource("gpu", 2)
    

Create a resource profile.
    
    
    >>> builder = ResourceProfileBuilder()
    >>> resource_profile = builder.require(executor_requests).require(task_requests).build
    

Create an RDD with the resource profile.
    
    
    >>> rdd = sc.parallelize(range(10)).withResources(resource_profile)
    >>> rdd.getResourceProfile()
    <pyspark.resource.profile.ResourceProfile object ...>
    >>> rdd.getResourceProfile().taskResources
    {'cpus': <...TaskResourceRequest...>, 'gpu': <...TaskResourceRequest...>}
    >>> rdd.getResourceProfile().executorResources
    {'gpu': <...ExecutorResourceRequest...>,
     'cores': <...ExecutorResourceRequest...>,
     'offHeap': <...ExecutorResourceRequest...>,
     'memoryOverhead': <...ExecutorResourceRequest...>,
     'pyspark.memory': <...ExecutorResourceRequest...>,
     'memory': <...ExecutorResourceRequest...>}
    

Attributes

`executorResources` | 

Returns
      
---|---  
`id` | 

Returns
      
`taskResources` | 

Returns
      
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.ResourceProfile.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.ResourceProfileBuilder.html

# pyspark.resource.ResourceProfileBuilder#

_class _pyspark.resource.ResourceProfileBuilder[[source]](../../_modules/pyspark/resource/profile.html#ResourceProfileBuilder)#
    

Resource profile Builder to build a resource profile to associate with an RDD. A ResourceProfile allows the user to specify executor and task requirements for an RDD that will get applied during a stage. This allows the user to change the resource requirements between stages.

New in version 3.1.0.

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Methods

`clearExecutorResourceRequests`() |   
---|---  
`clearTaskResourceRequests`() |   
`require`(resourceRequest) | Add executor resource requests  
  
Attributes

`build` |   
---|---  
`executorResources` | 

Returns
      
`taskResources` | 

Returns
      
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.ResourceProfileBuilder.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.ExecutorResourceRequest.html

# pyspark.resource.ExecutorResourceRequest#

_class _pyspark.resource.ExecutorResourceRequest(_resourceName_ , _amount_ , _discoveryScript =''_, _vendor =''_)[[source]](../../_modules/pyspark/resource/requests.html#ExecutorResourceRequest)#
    

An Executor resource request. This is used in conjunction with the ResourceProfile to programmatically specify the resources needed for an RDD that will be applied at the stage level.

This is used to specify what the resource requirements are for an Executor and how Spark can find out specific details about those resources. Not all the parameters are required for every resource type. Resources like GPUs are supported and have same limitations as using the global spark configs spark.executor.resource.gpu.*. The amount, discoveryScript, and vendor parameters for resources are all the same parameters a user would specify through the configs: spark.executor.resource.{resourceName}.{amount, discoveryScript, vendor}.

For instance, a user wants to allocate an Executor with GPU resources on YARN. The user has to specify the resource name (gpu), the amount or number of GPUs per Executor, the discovery script would be specified so that when the Executor starts up it can discovery what GPU addresses are available for it to use because YARN doesnât tell Spark that, then vendor would not be used because its specific for Kubernetes.

See the configuration and cluster specific docs for more details.

Use `pyspark.ExecutorResourceRequests` class as a convenience API.

New in version 3.1.0.

Parameters
    

**resourceName** str
    

Name of the resource

**amount** str
    

Amount requesting

**discoveryScript** str, optional
    

Optional script used to discover the resources. This is required on some cluster managers that donât tell Spark the addresses of the resources allocated. The script runs on Executors startup to discover the addresses of the resources available.

**vendor** str, optional
    

Vendor, required for some cluster managers

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Attributes

`amount` | 

Returns
      
---|---  
`discoveryScript` | 

Returns
      
`resourceName` | 

Returns
      
`vendor` | 

Returns
      
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.ExecutorResourceRequest.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.ExecutorResourceRequests.html

# pyspark.resource.ExecutorResourceRequests#

_class _pyspark.resource.ExecutorResourceRequests(__jvm =None_, __requests =None_)[[source]](../../_modules/pyspark/resource/requests.html#ExecutorResourceRequests)#
    

A set of Executor resource requests. This is used in conjunction with the [`pyspark.resource.ResourceProfileBuilder`](pyspark.resource.ResourceProfileBuilder.html#pyspark.resource.ResourceProfileBuilder "pyspark.resource.ResourceProfileBuilder") to programmatically specify the resources needed for an RDD that will be applied at the stage level.

New in version 3.1.0.

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Methods

`cores`(amount) | Specify number of cores per Executor.  
---|---  
`memory`(amount) | Specify heap memory.  
`memoryOverhead`(amount) | Specify overhead memory.  
`offheapMemory`(amount) | Specify off heap memory.  
`pysparkMemory`(amount) | Specify pyspark memory.  
`resource`(resourceName,Â amount[,Â ...]) | Amount of a particular custom resource(GPU, FPGA, etc) to use.  
  
Attributes

`requests` | 

Returns
      
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.ExecutorResourceRequests.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.TaskResourceRequest.html

# pyspark.resource.TaskResourceRequest#

_class _pyspark.resource.TaskResourceRequest(_resourceName_ , _amount_)[[source]](../../_modules/pyspark/resource/requests.html#TaskResourceRequest)#
    

A task resource request. This is used in conjunction with the [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") to programmatically specify the resources needed for an RDD that will be applied at the stage level. The amount is specified as a float to allow for saying you want more than 1 task per resource. Valid values are less than or equal to 0.5 or whole numbers. Use [`pyspark.resource.TaskResourceRequests`](pyspark.resource.TaskResourceRequests.html#pyspark.resource.TaskResourceRequests "pyspark.resource.TaskResourceRequests") class as a convenience API.

Parameters
    

**resourceName** str
    

Name of the resource

**amount** float
    

Amount requesting as a float to support fractional resource requests. Valid values are less than or equal to 0.5 or whole numbers. This essentially lets you configure X number of tasks to run on a single resource, ie amount equals 0.5 translates into 2 tasks per resource address.

**.. versionadded:: 3.1.0**
    

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Attributes

`amount` | 

Returns
      
---|---  
`resourceName` | 

Returns
      
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.TaskResourceRequest.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.resource.TaskResourceRequests.html

# pyspark.resource.TaskResourceRequests#

_class _pyspark.resource.TaskResourceRequests(__jvm =None_, __requests =None_)[[source]](../../_modules/pyspark/resource/requests.html#TaskResourceRequests)#
    

A set of task resource requests. This is used in conjunction with the [`pyspark.resource.ResourceProfileBuilder`](pyspark.resource.ResourceProfileBuilder.html#pyspark.resource.ResourceProfileBuilder "pyspark.resource.ResourceProfileBuilder") to programmatically specify the resources needed for an RDD that will be applied at the stage level.

New in version 3.1.0.

See also

[`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

Notes

This API is evolving.

Methods

`cpus`(amount) | Specify number of cpus per Task.  
---|---  
`resource`(resourceName,Â amount) | Amount of a particular custom resource(GPU, FPGA, etc) to use.  
  
Attributes

`requests` | 

Returns
      
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.resource.TaskResourceRequests.rst.txt)
