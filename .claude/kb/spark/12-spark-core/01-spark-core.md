# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.html

# Spark Core#

## Public Classes#

[`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext")([master,Â appName,Â sparkHome,Â ...]) | Main entry point for Spark functionality.  
---|---  
[`RDD`](api/pyspark.RDD.html#pyspark.RDD "pyspark.RDD")(jrdd,Â ctx[,Â jrdd_deserializer]) | A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.  
[`Broadcast`](api/pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast")([sc,Â value,Â pickle_registry,Â ...]) | A broadcast variable created with [`SparkContext.broadcast()`](api/pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast").  
[`Accumulator`](api/pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator")(aid,Â value,Â accum_param) | A shared variable that can be accumulated, i.e., has a commutative and associative "add" operation.  
[`AccumulatorParam`](api/pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam")() | Helper object that defines how to accumulate values of a given type.  
[`SparkConf`](api/pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf")([loadDefaults,Â _jvm,Â _jconf]) | Configuration for a Spark application.  
[`SparkFiles`](api/pyspark.SparkFiles.html#pyspark.SparkFiles "pyspark.SparkFiles")() | Resolves paths to files added through [`SparkContext.addFile()`](api/pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile").  
[`StorageLevel`](api/pyspark.StorageLevel.html#pyspark.StorageLevel "pyspark.StorageLevel")(useDisk,Â useMemory,Â useOffHeap,Â ...) | Flags for controlling the storage of an RDD.  
[`TaskContext`](api/pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext")() | Contextual information about a task which can be read or mutated during execution.  
[`RDDBarrier`](api/pyspark.RDDBarrier.html#pyspark.RDDBarrier "pyspark.RDDBarrier")(rdd) | Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.  
[`BarrierTaskContext`](api/pyspark.BarrierTaskContext.html#pyspark.BarrierTaskContext "pyspark.BarrierTaskContext")() | A [`TaskContext`](api/pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage.  
[`BarrierTaskInfo`](api/pyspark.BarrierTaskInfo.html#pyspark.BarrierTaskInfo "pyspark.BarrierTaskInfo")(address) | Carries all task infos of a barrier task.  
[`InheritableThread`](api/pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread")(target,Â *args[,Â session]) | Thread that is recommended to be used in PySpark when the pinned thread mode is enabled.  
[`util.VersionUtils`](api/pyspark.util.VersionUtils.html#pyspark.util.VersionUtils "pyspark.util.VersionUtils")() | Provides utility method to determine Spark versions with given input string.  
  
## Spark Context APIs#

[`SparkContext.PACKAGE_EXTENSIONS`](api/pyspark.SparkContext.PACKAGE_EXTENSIONS.html#pyspark.SparkContext.PACKAGE_EXTENSIONS "pyspark.SparkContext.PACKAGE_EXTENSIONS") |   
---|---  
[`SparkContext.accumulator`](api/pyspark.SparkContext.accumulator.html#pyspark.SparkContext.accumulator "pyspark.SparkContext.accumulator")(value[,Â accum_param]) | Create an [`Accumulator`](api/pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator") with the given initial value, using a given [`AccumulatorParam`](api/pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") helper object to define how to add values of the data type if provided.  
[`SparkContext.addArchive`](api/pyspark.SparkContext.addArchive.html#pyspark.SparkContext.addArchive "pyspark.SparkContext.addArchive")(path) | Add an archive to be downloaded with this Spark job on every node.  
[`SparkContext.addFile`](api/pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")(path[,Â recursive]) | Add a file to be downloaded with this Spark job on every node.  
[`SparkContext.addJobTag`](api/pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")(tag) | Add a tag to be assigned to all the jobs started by this thread.  
[`SparkContext.addPyFile`](api/pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")(path) | Add a .py or .zip dependency for all tasks to be executed on this SparkContext in the future.  
[`SparkContext.applicationId`](api/pyspark.SparkContext.applicationId.html#pyspark.SparkContext.applicationId "pyspark.SparkContext.applicationId") | A unique identifier for the Spark application.  
[`SparkContext.binaryFiles`](api/pyspark.SparkContext.binaryFiles.html#pyspark.SparkContext.binaryFiles "pyspark.SparkContext.binaryFiles")(path[,Â minPartitions]) | Read a directory of binary files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI as a byte array.  
[`SparkContext.binaryRecords`](api/pyspark.SparkContext.binaryRecords.html#pyspark.SparkContext.binaryRecords "pyspark.SparkContext.binaryRecords")(path,Â recordLength) | Load data from a flat binary file, assuming each record is a set of numbers with the specified numerical format (see ByteBuffer), and the number of bytes per record is constant.  
[`SparkContext.broadcast`](api/pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast")(value) | Broadcast a read-only variable to the cluster, returning a [`Broadcast`](api/pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object for reading it in distributed functions.  
[`SparkContext.cancelAllJobs`](api/pyspark.SparkContext.cancelAllJobs.html#pyspark.SparkContext.cancelAllJobs "pyspark.SparkContext.cancelAllJobs")() | Cancel all jobs that have been scheduled or are running.  
[`SparkContext.cancelJobGroup`](api/pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")(groupId) | Cancel active jobs for the specified group.  
[`SparkContext.cancelJobsWithTag`](api/pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")(tag) | Cancel active jobs that have the specified tag.  
[`SparkContext.clearJobTags`](api/pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")() | Clear the current thread's job tags.  
[`SparkContext.defaultMinPartitions`](api/pyspark.SparkContext.defaultMinPartitions.html#pyspark.SparkContext.defaultMinPartitions "pyspark.SparkContext.defaultMinPartitions") | Default min number of partitions for Hadoop RDDs when not given by user  
[`SparkContext.defaultParallelism`](api/pyspark.SparkContext.defaultParallelism.html#pyspark.SparkContext.defaultParallelism "pyspark.SparkContext.defaultParallelism") | Default level of parallelism to use when not given by user (e.g.  
[`SparkContext.dump_profiles`](api/pyspark.SparkContext.dump_profiles.html#pyspark.SparkContext.dump_profiles "pyspark.SparkContext.dump_profiles")(path) | Dump the profile stats into directory path  
[`SparkContext.emptyRDD`](api/pyspark.SparkContext.emptyRDD.html#pyspark.SparkContext.emptyRDD "pyspark.SparkContext.emptyRDD")() | Create an [`RDD`](api/pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that has no partitions or elements.  
[`SparkContext.getCheckpointDir`](api/pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")() | Return the directory where RDDs are checkpointed.  
[`SparkContext.getConf`](api/pyspark.SparkContext.getConf.html#pyspark.SparkContext.getConf "pyspark.SparkContext.getConf")() | Return a copy of this SparkContext's configuration [`SparkConf`](api/pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf").  
[`SparkContext.getJobTags`](api/pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")() | Get the tags that are currently set to be assigned to all the jobs started by this thread.  
[`SparkContext.getLocalProperty`](api/pyspark.SparkContext.getLocalProperty.html#pyspark.SparkContext.getLocalProperty "pyspark.SparkContext.getLocalProperty")(key) | Get a local property set in this thread, or null if it is missing.  
[`SparkContext.getOrCreate`](api/pyspark.SparkContext.getOrCreate.html#pyspark.SparkContext.getOrCreate "pyspark.SparkContext.getOrCreate")([conf]) | Get or instantiate a [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") and register it as a singleton object.  
[`SparkContext.getSystemProperty`](api/pyspark.SparkContext.getSystemProperty.html#pyspark.SparkContext.getSystemProperty "pyspark.SparkContext.getSystemProperty")(key) | Get a Java system property, such as java.home.  
[`SparkContext.hadoopFile`](api/pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")(path,Â ...[,Â ...]) | Read an 'old' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`SparkContext.hadoopRDD`](api/pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")(inputFormatClass,Â ...) | Read an 'old' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`SparkContext.listArchives`](api/pyspark.SparkContext.listArchives.html#pyspark.SparkContext.listArchives "pyspark.SparkContext.listArchives") | Returns a list of archive paths that are added to resources.  
[`SparkContext.listFiles`](api/pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles") | Returns a list of file paths that are added to resources.  
[`SparkContext.newAPIHadoopFile`](api/pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")(path,Â ...[,Â ...]) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`SparkContext.newAPIHadoopRDD`](api/pyspark.SparkContext.newAPIHadoopRDD.html#pyspark.SparkContext.newAPIHadoopRDD "pyspark.SparkContext.newAPIHadoopRDD")(...[,Â ...]) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`SparkContext.parallelize`](api/pyspark.SparkContext.parallelize.html#pyspark.SparkContext.parallelize "pyspark.SparkContext.parallelize")(c[,Â numSlices]) | Distribute a local Python collection to form an RDD.  
[`SparkContext.pickleFile`](api/pyspark.SparkContext.pickleFile.html#pyspark.SparkContext.pickleFile "pyspark.SparkContext.pickleFile")(name[,Â minPartitions]) | Load an RDD previously saved using [`RDD.saveAsPickleFile()`](api/pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile") method.  
[`SparkContext.range`](api/pyspark.SparkContext.range.html#pyspark.SparkContext.range "pyspark.SparkContext.range")(start[,Â end,Â step,Â numSlices]) | Create a new RDD of int containing elements from start to end (exclusive), increased by step every element.  
[`SparkContext.resources`](api/pyspark.SparkContext.resources.html#pyspark.SparkContext.resources "pyspark.SparkContext.resources") | Return the resource information of this [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext").  
[`SparkContext.removeJobTag`](api/pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")(tag) | Remove a tag previously added to be assigned to all the jobs started by this thread.  
[`SparkContext.runJob`](api/pyspark.SparkContext.runJob.html#pyspark.SparkContext.runJob "pyspark.SparkContext.runJob")(rdd,Â partitionFunc[,Â ...]) | Executes the given partitionFunc on the specified set of partitions, returning the result as an array of elements.  
[`SparkContext.sequenceFile`](api/pyspark.SparkContext.sequenceFile.html#pyspark.SparkContext.sequenceFile "pyspark.SparkContext.sequenceFile")(path[,Â keyClass,Â ...]) | Read a Hadoop SequenceFile with arbitrary key and value Writable class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`SparkContext.setCheckpointDir`](api/pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")(dirName) | Set the directory under which RDDs are going to be checkpointed.  
[`SparkContext.setInterruptOnCancel`](api/pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")(...) | Set the behavior of job cancellation from jobs started in this thread.  
[`SparkContext.setJobDescription`](api/pyspark.SparkContext.setJobDescription.html#pyspark.SparkContext.setJobDescription "pyspark.SparkContext.setJobDescription")(value) | Set a human readable description of the current job.  
[`SparkContext.setJobGroup`](api/pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")(groupId,Â description) | Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.  
[`SparkContext.setLocalProperty`](api/pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty")(key,Â value) | Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.  
[`SparkContext.setLogLevel`](api/pyspark.SparkContext.setLogLevel.html#pyspark.SparkContext.setLogLevel "pyspark.SparkContext.setLogLevel")(logLevel) | Control our logLevel.  
[`SparkContext.setSystemProperty`](api/pyspark.SparkContext.setSystemProperty.html#pyspark.SparkContext.setSystemProperty "pyspark.SparkContext.setSystemProperty")(key,Â value) | Set a Java system property, such as spark.executor.memory.  
[`SparkContext.show_profiles`](api/pyspark.SparkContext.show_profiles.html#pyspark.SparkContext.show_profiles "pyspark.SparkContext.show_profiles")() | Print the profile stats to stdout  
[`SparkContext.sparkUser`](api/pyspark.SparkContext.sparkUser.html#pyspark.SparkContext.sparkUser "pyspark.SparkContext.sparkUser")() | Get SPARK_USER for user who is running SparkContext.  
[`SparkContext.startTime`](api/pyspark.SparkContext.startTime.html#pyspark.SparkContext.startTime "pyspark.SparkContext.startTime") | Return the epoch time when the [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") was started.  
[`SparkContext.statusTracker`](api/pyspark.SparkContext.statusTracker.html#pyspark.SparkContext.statusTracker "pyspark.SparkContext.statusTracker")() | Return `StatusTracker` object  
[`SparkContext.stop`](api/pyspark.SparkContext.stop.html#pyspark.SparkContext.stop "pyspark.SparkContext.stop")() | Shut down the [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext").  
[`SparkContext.textFile`](api/pyspark.SparkContext.textFile.html#pyspark.SparkContext.textFile "pyspark.SparkContext.textFile")(name[,Â minPartitions,Â ...]) | Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings.  
[`SparkContext.uiWebUrl`](api/pyspark.SparkContext.uiWebUrl.html#pyspark.SparkContext.uiWebUrl "pyspark.SparkContext.uiWebUrl") | Return the URL of the SparkUI instance started by this [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext")  
[`SparkContext.union`](api/pyspark.SparkContext.union.html#pyspark.SparkContext.union "pyspark.SparkContext.union")(rdds) | Build the union of a list of RDDs.  
[`SparkContext.version`](api/pyspark.SparkContext.version.html#pyspark.SparkContext.version "pyspark.SparkContext.version") | The version of Spark on which this application is running.  
[`SparkContext.wholeTextFiles`](api/pyspark.SparkContext.wholeTextFiles.html#pyspark.SparkContext.wholeTextFiles "pyspark.SparkContext.wholeTextFiles")(path[,Â ...]) | Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
  
## RDD APIs#

[`RDD.aggregate`](api/pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")(zeroValue,Â seqOp,Â combOp) | Aggregate the elements of each partition, and then the results for all the partitions, using a given combine functions and a neutral "zero value."  
---|---  
[`RDD.aggregateByKey`](api/pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")(zeroValue,Â seqFunc,Â combFunc) | Aggregate the values of each key, using given combine functions and a neutral "zero value".  
[`RDD.barrier`](api/pyspark.RDD.barrier.html#pyspark.RDD.barrier "pyspark.RDD.barrier")() | Marks the current stage as a barrier stage, where Spark must launch all tasks together.  
[`RDD.cache`](api/pyspark.RDD.cache.html#pyspark.RDD.cache "pyspark.RDD.cache")() | Persist this RDD with the default storage level (MEMORY_ONLY).  
[`RDD.cartesian`](api/pyspark.RDD.cartesian.html#pyspark.RDD.cartesian "pyspark.RDD.cartesian")(other) | Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements `(a, b)` where `a` is in self and `b` is in other.  
[`RDD.checkpoint`](api/pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")() | Mark this RDD for checkpointing.  
[`RDD.cleanShuffleDependencies`](api/pyspark.RDD.cleanShuffleDependencies.html#pyspark.RDD.cleanShuffleDependencies "pyspark.RDD.cleanShuffleDependencies")([blocking]) | Removes an RDD's shuffles and it's non-persisted ancestors.  
[`RDD.coalesce`](api/pyspark.RDD.coalesce.html#pyspark.RDD.coalesce "pyspark.RDD.coalesce")(numPartitions[,Â shuffle]) | Return a new RDD that is reduced into numPartitions partitions.  
[`RDD.cogroup`](api/pyspark.RDD.cogroup.html#pyspark.RDD.cogroup "pyspark.RDD.cogroup")(other[,Â numPartitions]) | For each key k in self or other, return a resulting RDD that contains a tuple with the list of values for that key in self as well as other.  
[`RDD.collect`](api/pyspark.RDD.collect.html#pyspark.RDD.collect "pyspark.RDD.collect")() | Return a list that contains all the elements in this RDD.  
[`RDD.collectAsMap`](api/pyspark.RDD.collectAsMap.html#pyspark.RDD.collectAsMap "pyspark.RDD.collectAsMap")() | Return the key-value pairs in this RDD to the master as a dictionary.  
[`RDD.collectWithJobGroup`](api/pyspark.RDD.collectWithJobGroup.html#pyspark.RDD.collectWithJobGroup "pyspark.RDD.collectWithJobGroup")(groupId,Â description) | When collect rdd, use this method to specify job group.  
[`RDD.combineByKey`](api/pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")(createCombiner,Â mergeValue,Â ...) | Generic function to combine the elements for each key using a custom set of aggregation functions.  
[`RDD.context`](api/pyspark.RDD.context.html#pyspark.RDD.context "pyspark.RDD.context") | The [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") that this RDD was created on.  
[`RDD.count`](api/pyspark.RDD.count.html#pyspark.RDD.count "pyspark.RDD.count")() | Return the number of elements in this RDD.  
[`RDD.countApprox`](api/pyspark.RDD.countApprox.html#pyspark.RDD.countApprox "pyspark.RDD.countApprox")(timeout[,Â confidence]) | Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.  
[`RDD.countApproxDistinct`](api/pyspark.RDD.countApproxDistinct.html#pyspark.RDD.countApproxDistinct "pyspark.RDD.countApproxDistinct")([relativeSD]) | Return approximate number of distinct elements in the RDD.  
[`RDD.countByKey`](api/pyspark.RDD.countByKey.html#pyspark.RDD.countByKey "pyspark.RDD.countByKey")() | Count the number of elements for each key, and return the result to the master as a dictionary.  
[`RDD.countByValue`](api/pyspark.RDD.countByValue.html#pyspark.RDD.countByValue "pyspark.RDD.countByValue")() | Return the count of each unique value in this RDD as a dictionary of (value, count) pairs.  
[`RDD.distinct`](api/pyspark.RDD.distinct.html#pyspark.RDD.distinct "pyspark.RDD.distinct")([numPartitions]) | Return a new RDD containing the distinct elements in this RDD.  
[`RDD.filter`](api/pyspark.RDD.filter.html#pyspark.RDD.filter "pyspark.RDD.filter")(f) | Return a new RDD containing only the elements that satisfy a predicate.  
[`RDD.first`](api/pyspark.RDD.first.html#pyspark.RDD.first "pyspark.RDD.first")() | Return the first element in this RDD.  
[`RDD.flatMap`](api/pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")(f[,Â preservesPartitioning]) | Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  
[`RDD.flatMapValues`](api/pyspark.RDD.flatMapValues.html#pyspark.RDD.flatMapValues "pyspark.RDD.flatMapValues")(f) | Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDD's partitioning.  
[`RDD.fold`](api/pyspark.RDD.fold.html#pyspark.RDD.fold "pyspark.RDD.fold")(zeroValue,Â op) | Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value."  
[`RDD.foldByKey`](api/pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")(zeroValue,Â func[,Â ...]) | Merge the values for each key using an associative function "func" and a neutral "zeroValue" which may be added to the result an arbitrary number of times, and must not change the result (e.g., 0 for addition, or 1 for multiplication.).  
[`RDD.foreach`](api/pyspark.RDD.foreach.html#pyspark.RDD.foreach "pyspark.RDD.foreach")(f) | Applies a function to all elements of this RDD.  
[`RDD.foreachPartition`](api/pyspark.RDD.foreachPartition.html#pyspark.RDD.foreachPartition "pyspark.RDD.foreachPartition")(f) | Applies a function to each partition of this RDD.  
[`RDD.fullOuterJoin`](api/pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`RDD.getCheckpointFile`](api/pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")() | Gets the name of the file to which this RDD was checkpointed  
[`RDD.getNumPartitions`](api/pyspark.RDD.getNumPartitions.html#pyspark.RDD.getNumPartitions "pyspark.RDD.getNumPartitions")() | Returns the number of partitions in RDD  
[`RDD.getResourceProfile`](api/pyspark.RDD.getResourceProfile.html#pyspark.RDD.getResourceProfile "pyspark.RDD.getResourceProfile")() | Get the [`pyspark.resource.ResourceProfile`](api/pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") specified with this RDD or None if it wasn't specified.  
[`RDD.getStorageLevel`](api/pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")() | Get the RDD's current storage level.  
[`RDD.glom`](api/pyspark.RDD.glom.html#pyspark.RDD.glom "pyspark.RDD.glom")() | Return an RDD created by coalescing all elements within each partition into a list.  
[`RDD.groupBy`](api/pyspark.RDD.groupBy.html#pyspark.RDD.groupBy "pyspark.RDD.groupBy")(f[,Â numPartitions,Â partitionFunc]) | Return an RDD of grouped items.  
[`RDD.groupByKey`](api/pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")([numPartitions,Â partitionFunc]) | Group the values for each key in the RDD into a single sequence.  
[`RDD.groupWith`](api/pyspark.RDD.groupWith.html#pyspark.RDD.groupWith "pyspark.RDD.groupWith")(other,Â *others) | Alias for cogroup but with support for multiple RDDs.  
[`RDD.histogram`](api/pyspark.RDD.histogram.html#pyspark.RDD.histogram "pyspark.RDD.histogram")(buckets) | Compute a histogram using the provided buckets.  
[`RDD.id`](api/pyspark.RDD.id.html#pyspark.RDD.id "pyspark.RDD.id")() | A unique ID for this RDD (within its SparkContext).  
[`RDD.intersection`](api/pyspark.RDD.intersection.html#pyspark.RDD.intersection "pyspark.RDD.intersection")(other) | Return the intersection of this RDD and another one.  
[`RDD.isCheckpointed`](api/pyspark.RDD.isCheckpointed.html#pyspark.RDD.isCheckpointed "pyspark.RDD.isCheckpointed")() | Return whether this RDD is checkpointed and materialized, either reliably or locally.  
[`RDD.isEmpty`](api/pyspark.RDD.isEmpty.html#pyspark.RDD.isEmpty "pyspark.RDD.isEmpty")() | Returns true if and only if the RDD contains no elements at all.  
[`RDD.isLocallyCheckpointed`](api/pyspark.RDD.isLocallyCheckpointed.html#pyspark.RDD.isLocallyCheckpointed "pyspark.RDD.isLocallyCheckpointed")() | Return whether this RDD is marked for local checkpointing.  
[`RDD.join`](api/pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")(other[,Â numPartitions]) | Return an RDD containing all pairs of elements with matching keys in self and other.  
[`RDD.keyBy`](api/pyspark.RDD.keyBy.html#pyspark.RDD.keyBy "pyspark.RDD.keyBy")(f) | Creates tuples of the elements in this RDD by applying f.  
[`RDD.keys`](api/pyspark.RDD.keys.html#pyspark.RDD.keys "pyspark.RDD.keys")() | Return an RDD with the keys of each tuple.  
[`RDD.leftOuterJoin`](api/pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")(other[,Â numPartitions]) | Perform a left outer join of self and other.  
[`RDD.localCheckpoint`](api/pyspark.RDD.localCheckpoint.html#pyspark.RDD.localCheckpoint "pyspark.RDD.localCheckpoint")() | Mark this RDD for local checkpointing using Spark's existing caching layer.  
[`RDD.lookup`](api/pyspark.RDD.lookup.html#pyspark.RDD.lookup "pyspark.RDD.lookup")(key) | Return the list of values in the RDD for key key.  
[`RDD.map`](api/pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each element of this RDD.  
[`RDD.mapPartitions`](api/pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each partition of this RDD.  
[`RDD.mapPartitionsWithIndex`](api/pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`RDD.mapPartitionsWithSplit`](api/pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`RDD.mapValues`](api/pyspark.RDD.mapValues.html#pyspark.RDD.mapValues "pyspark.RDD.mapValues")(f) | Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD's partitioning.  
[`RDD.max`](api/pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")([key]) | Find the maximum item in this RDD.  
[`RDD.mean`](api/pyspark.RDD.mean.html#pyspark.RDD.mean "pyspark.RDD.mean")() | Compute the mean of this RDD's elements.  
[`RDD.meanApprox`](api/pyspark.RDD.meanApprox.html#pyspark.RDD.meanApprox "pyspark.RDD.meanApprox")(timeout[,Â confidence]) | Approximate operation to return the mean within a timeout or meet the confidence.  
[`RDD.min`](api/pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")([key]) | Find the minimum item in this RDD.  
[`RDD.name`](api/pyspark.RDD.name.html#pyspark.RDD.name "pyspark.RDD.name")() | Return the name of this RDD.  
[`RDD.partitionBy`](api/pyspark.RDD.partitionBy.html#pyspark.RDD.partitionBy "pyspark.RDD.partitionBy")(numPartitions[,Â partitionFunc]) | Return a copy of the RDD partitioned using the specified partitioner.  
[`RDD.persist`](api/pyspark.RDD.persist.html#pyspark.RDD.persist "pyspark.RDD.persist")([storageLevel]) | Set this RDD's storage level to persist its values across operations after the first time it is computed.  
[`RDD.pipe`](api/pyspark.RDD.pipe.html#pyspark.RDD.pipe "pyspark.RDD.pipe")(command[,Â env,Â checkCode]) | Return an RDD created by piping elements to a forked external process.  
[`RDD.randomSplit`](api/pyspark.RDD.randomSplit.html#pyspark.RDD.randomSplit "pyspark.RDD.randomSplit")(weights[,Â seed]) | Randomly splits this RDD with the provided weights.  
[`RDD.reduce`](api/pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")(f) | Reduces the elements of this RDD using the specified commutative and associative binary operator.  
[`RDD.reduceByKey`](api/pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")(func[,Â numPartitions,Â ...]) | Merge the values for each key using an associative and commutative reduce function.  
[`RDD.reduceByKeyLocally`](api/pyspark.RDD.reduceByKeyLocally.html#pyspark.RDD.reduceByKeyLocally "pyspark.RDD.reduceByKeyLocally")(func) | Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a dictionary.  
[`RDD.repartition`](api/pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")(numPartitions) | Return a new RDD that has exactly numPartitions partitions.  
[`RDD.repartitionAndSortWithinPartitions`](api/pyspark.RDD.repartitionAndSortWithinPartitions.html#pyspark.RDD.repartitionAndSortWithinPartitions "pyspark.RDD.repartitionAndSortWithinPartitions")([...]) | Repartition the RDD according to the given partitioner and, within each resulting partition, sort records by their keys.  
[`RDD.rightOuterJoin`](api/pyspark.RDD.rightOuterJoin.html#pyspark.RDD.rightOuterJoin "pyspark.RDD.rightOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`RDD.sample`](api/pyspark.RDD.sample.html#pyspark.RDD.sample "pyspark.RDD.sample")(withReplacement,Â fraction[,Â seed]) | Return a sampled subset of this RDD.  
[`RDD.sampleByKey`](api/pyspark.RDD.sampleByKey.html#pyspark.RDD.sampleByKey "pyspark.RDD.sampleByKey")(withReplacement,Â fractions) | Return a subset of this RDD sampled by key (via stratified sampling).  
[`RDD.sampleStdev`](api/pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")() | Compute the sample standard deviation of this RDD's elements (which corrects for bias in estimating the standard deviation by dividing by N-1 instead of N).  
[`RDD.sampleVariance`](api/pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")() | Compute the sample variance of this RDD's elements (which corrects for bias in estimating the variance by dividing by N-1 instead of N).  
[`RDD.saveAsHadoopDataset`](api/pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")(conf[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`RDD.saveAsHadoopFile`](api/pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")(path,Â outputFormatClass) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`RDD.saveAsNewAPIHadoopDataset`](api/pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")(conf[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`RDD.saveAsNewAPIHadoopFile`](api/pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")(path,Â ...[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`RDD.saveAsPickleFile`](api/pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile")(path[,Â batchSize]) | Save this RDD as a SequenceFile of serialized objects.  
[`RDD.saveAsSequenceFile`](api/pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")(path[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the "org.apache.hadoop.io.Writable" types that we convert from the RDD's key and value types.  
[`RDD.saveAsTextFile`](api/pyspark.RDD.saveAsTextFile.html#pyspark.RDD.saveAsTextFile "pyspark.RDD.saveAsTextFile")(path[,Â compressionCodecClass]) | Save this RDD as a text file, using string representations of elements.  
[`RDD.setName`](api/pyspark.RDD.setName.html#pyspark.RDD.setName "pyspark.RDD.setName")(name) | Assign a name to this RDD.  
[`RDD.sortBy`](api/pyspark.RDD.sortBy.html#pyspark.RDD.sortBy "pyspark.RDD.sortBy")(keyfunc[,Â ascending,Â numPartitions]) | Sorts this RDD by the given keyfunc  
[`RDD.sortByKey`](api/pyspark.RDD.sortByKey.html#pyspark.RDD.sortByKey "pyspark.RDD.sortByKey")([ascending,Â numPartitions,Â ...]) | Sorts this RDD, which is assumed to consist of (key, value) pairs.  
[`RDD.stats`](api/pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")() | Return a `StatCounter` object that captures the mean, variance and count of the RDD's elements in one operation.  
[`RDD.stdev`](api/pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")() | Compute the standard deviation of this RDD's elements.  
[`RDD.subtract`](api/pyspark.RDD.subtract.html#pyspark.RDD.subtract "pyspark.RDD.subtract")(other[,Â numPartitions]) | Return each value in self that is not contained in other.  
[`RDD.subtractByKey`](api/pyspark.RDD.subtractByKey.html#pyspark.RDD.subtractByKey "pyspark.RDD.subtractByKey")(other[,Â numPartitions]) | Return each (key, value) pair in self that has no pair with matching key in other.  
[`RDD.sum`](api/pyspark.RDD.sum.html#pyspark.RDD.sum "pyspark.RDD.sum")() | Add up the elements in this RDD.  
[`RDD.sumApprox`](api/pyspark.RDD.sumApprox.html#pyspark.RDD.sumApprox "pyspark.RDD.sumApprox")(timeout[,Â confidence]) | Approximate operation to return the sum within a timeout or meet the confidence.  
[`RDD.take`](api/pyspark.RDD.take.html#pyspark.RDD.take "pyspark.RDD.take")(num) | Take the first num elements of the RDD.  
[`RDD.takeOrdered`](api/pyspark.RDD.takeOrdered.html#pyspark.RDD.takeOrdered "pyspark.RDD.takeOrdered")(num[,Â key]) | Get the N elements from an RDD ordered in ascending order or as specified by the optional key function.  
[`RDD.takeSample`](api/pyspark.RDD.takeSample.html#pyspark.RDD.takeSample "pyspark.RDD.takeSample")(withReplacement,Â num[,Â seed]) | Return a fixed-size sampled subset of this RDD.  
[`RDD.toDebugString`](api/pyspark.RDD.toDebugString.html#pyspark.RDD.toDebugString "pyspark.RDD.toDebugString")() | A description of this RDD and its recursive dependencies for debugging.  
[`RDD.toLocalIterator`](api/pyspark.RDD.toLocalIterator.html#pyspark.RDD.toLocalIterator "pyspark.RDD.toLocalIterator")([prefetchPartitions]) | Return an iterator that contains all of the elements in this RDD.  
[`RDD.top`](api/pyspark.RDD.top.html#pyspark.RDD.top "pyspark.RDD.top")(num[,Â key]) | Get the top N elements from an RDD.  
[`RDD.treeAggregate`](api/pyspark.RDD.treeAggregate.html#pyspark.RDD.treeAggregate "pyspark.RDD.treeAggregate")(zeroValue,Â seqOp,Â combOp) | Aggregates the elements of this RDD in a multi-level tree pattern.  
[`RDD.treeReduce`](api/pyspark.RDD.treeReduce.html#pyspark.RDD.treeReduce "pyspark.RDD.treeReduce")(f[,Â depth]) | Reduces the elements of this RDD in a multi-level tree pattern.  
[`RDD.union`](api/pyspark.RDD.union.html#pyspark.RDD.union "pyspark.RDD.union")(other) | Return the union of this RDD and another one.  
[`RDD.unpersist`](api/pyspark.RDD.unpersist.html#pyspark.RDD.unpersist "pyspark.RDD.unpersist")([blocking]) | Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  
[`RDD.values`](api/pyspark.RDD.values.html#pyspark.RDD.values "pyspark.RDD.values")() | Return an RDD with the values of each tuple.  
[`RDD.variance`](api/pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")() | Compute the variance of this RDD's elements.  
[`RDD.withResources`](api/pyspark.RDD.withResources.html#pyspark.RDD.withResources "pyspark.RDD.withResources")(profile) | Specify a [`pyspark.resource.ResourceProfile`](api/pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") to use when calculating this RDD.  
[`RDD.zip`](api/pyspark.RDD.zip.html#pyspark.RDD.zip "pyspark.RDD.zip")(other) | Zips this RDD with another one, returning key-value pairs with the first element in each RDD second element in each RDD, etc.  
[`RDD.zipWithIndex`](api/pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex")() | Zips this RDD with its element indices.  
[`RDD.zipWithUniqueId`](api/pyspark.RDD.zipWithUniqueId.html#pyspark.RDD.zipWithUniqueId "pyspark.RDD.zipWithUniqueId")() | Zips this RDD with generated unique Long ids.  
  
## Broadcast and Accumulator#

[`Broadcast.destroy`](api/pyspark.Broadcast.destroy.html#pyspark.Broadcast.destroy "pyspark.Broadcast.destroy")([blocking]) | Destroy all data and metadata related to this broadcast variable.  
---|---  
[`Broadcast.dump`](api/pyspark.Broadcast.dump.html#pyspark.Broadcast.dump "pyspark.Broadcast.dump")(value,Â f) | Write a pickled representation of value to the open file or socket.  
[`Broadcast.load`](api/pyspark.Broadcast.load.html#pyspark.Broadcast.load "pyspark.Broadcast.load")(file) | Read a pickled representation of value from the open file or socket.  
[`Broadcast.load_from_path`](api/pyspark.Broadcast.load_from_path.html#pyspark.Broadcast.load_from_path "pyspark.Broadcast.load_from_path")(path) | Read the pickled representation of an object from the open file and return the reconstituted object hierarchy specified therein.  
[`Broadcast.unpersist`](api/pyspark.Broadcast.unpersist.html#pyspark.Broadcast.unpersist "pyspark.Broadcast.unpersist")([blocking]) | Delete cached copies of this broadcast on the executors.  
[`Broadcast.value`](api/pyspark.Broadcast.value.html#pyspark.Broadcast.value "pyspark.Broadcast.value") | Return the broadcasted value  
[`Accumulator.add`](api/pyspark.Accumulator.add.html#pyspark.Accumulator.add "pyspark.Accumulator.add")(term) | Adds a term to this accumulator's value  
[`Accumulator.value`](api/pyspark.Accumulator.value.html#pyspark.Accumulator.value "pyspark.Accumulator.value") | Get the accumulator's value; only usable in driver program  
[`AccumulatorParam.addInPlace`](api/pyspark.AccumulatorParam.addInPlace.html#pyspark.AccumulatorParam.addInPlace "pyspark.AccumulatorParam.addInPlace")(value1,Â value2) | Add two values of the accumulator's data type, returning a new value; for efficiency, can also update value1 in place and return it.  
[`AccumulatorParam.zero`](api/pyspark.AccumulatorParam.zero.html#pyspark.AccumulatorParam.zero "pyspark.AccumulatorParam.zero")(value) | Provide a "zero value" for the type, compatible in dimensions with the provided value (e.g., a zero vector)  
  
## Management#

[`inheritable_thread_target`](api/pyspark.inheritable_thread_target.html#pyspark.inheritable_thread_target "pyspark.inheritable_thread_target")([f]) | Return thread target wrapper which is recommended to be used in PySpark when the pinned thread mode is enabled.  
---|---  
[`SparkConf.contains`](api/pyspark.SparkConf.contains.html#pyspark.SparkConf.contains "pyspark.SparkConf.contains")(key) | Does this configuration contain a given key?  
[`SparkConf.get`](api/pyspark.SparkConf.get.html#pyspark.SparkConf.get "pyspark.SparkConf.get")(key[,Â defaultValue]) | Get the configured value for some key, or return a default otherwise.  
[`SparkConf.getAll`](api/pyspark.SparkConf.getAll.html#pyspark.SparkConf.getAll "pyspark.SparkConf.getAll")() | Get all values as a list of key-value pairs.  
[`SparkConf.set`](api/pyspark.SparkConf.set.html#pyspark.SparkConf.set "pyspark.SparkConf.set")(key,Â value) | Set a configuration property.  
[`SparkConf.setAll`](api/pyspark.SparkConf.setAll.html#pyspark.SparkConf.setAll "pyspark.SparkConf.setAll")(pairs) | Set multiple parameters, passed as a list of key-value pairs.  
[`SparkConf.setAppName`](api/pyspark.SparkConf.setAppName.html#pyspark.SparkConf.setAppName "pyspark.SparkConf.setAppName")(value) | Set application name.  
[`SparkConf.setExecutorEnv`](api/pyspark.SparkConf.setExecutorEnv.html#pyspark.SparkConf.setExecutorEnv "pyspark.SparkConf.setExecutorEnv")([key,Â value,Â pairs]) | Set an environment variable to be passed to executors.  
[`SparkConf.setIfMissing`](api/pyspark.SparkConf.setIfMissing.html#pyspark.SparkConf.setIfMissing "pyspark.SparkConf.setIfMissing")(key,Â value) | Set a configuration property, if not already set.  
[`SparkConf.setMaster`](api/pyspark.SparkConf.setMaster.html#pyspark.SparkConf.setMaster "pyspark.SparkConf.setMaster")(value) | Set master URL to connect to.  
[`SparkConf.setSparkHome`](api/pyspark.SparkConf.setSparkHome.html#pyspark.SparkConf.setSparkHome "pyspark.SparkConf.setSparkHome")(value) | Set path where Spark is installed on worker nodes.  
[`SparkConf.toDebugString`](api/pyspark.SparkConf.toDebugString.html#pyspark.SparkConf.toDebugString "pyspark.SparkConf.toDebugString")() | Returns a printable version of the configuration, as a list of key=value pairs, one per line.  
[`SparkFiles.get`](api/pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")(filename) | Get the absolute path of a file added through [`SparkContext.addFile()`](api/pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](api/pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
[`SparkFiles.getRootDirectory`](api/pyspark.SparkFiles.getRootDirectory.html#pyspark.SparkFiles.getRootDirectory "pyspark.SparkFiles.getRootDirectory")() | Get the root directory that contains files added through [`SparkContext.addFile()`](api/pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](api/pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
[`StorageLevel.DISK_ONLY`](api/pyspark.StorageLevel.DISK_ONLY.html#pyspark.StorageLevel.DISK_ONLY "pyspark.StorageLevel.DISK_ONLY") |   
[`StorageLevel.DISK_ONLY_2`](api/pyspark.StorageLevel.DISK_ONLY_2.html#pyspark.StorageLevel.DISK_ONLY_2 "pyspark.StorageLevel.DISK_ONLY_2") |   
[`StorageLevel.DISK_ONLY_3`](api/pyspark.StorageLevel.DISK_ONLY_3.html#pyspark.StorageLevel.DISK_ONLY_3 "pyspark.StorageLevel.DISK_ONLY_3") |   
[`StorageLevel.MEMORY_AND_DISK`](api/pyspark.StorageLevel.MEMORY_AND_DISK.html#pyspark.StorageLevel.MEMORY_AND_DISK "pyspark.StorageLevel.MEMORY_AND_DISK") |   
[`StorageLevel.MEMORY_AND_DISK_2`](api/pyspark.StorageLevel.MEMORY_AND_DISK_2.html#pyspark.StorageLevel.MEMORY_AND_DISK_2 "pyspark.StorageLevel.MEMORY_AND_DISK_2") |   
[`StorageLevel.MEMORY_AND_DISK_DESER`](api/pyspark.StorageLevel.MEMORY_AND_DISK_DESER.html#pyspark.StorageLevel.MEMORY_AND_DISK_DESER "pyspark.StorageLevel.MEMORY_AND_DISK_DESER") |   
[`StorageLevel.MEMORY_ONLY`](api/pyspark.StorageLevel.MEMORY_ONLY.html#pyspark.StorageLevel.MEMORY_ONLY "pyspark.StorageLevel.MEMORY_ONLY") |   
[`StorageLevel.MEMORY_ONLY_2`](api/pyspark.StorageLevel.MEMORY_ONLY_2.html#pyspark.StorageLevel.MEMORY_ONLY_2 "pyspark.StorageLevel.MEMORY_ONLY_2") |   
[`StorageLevel.OFF_HEAP`](api/pyspark.StorageLevel.OFF_HEAP.html#pyspark.StorageLevel.OFF_HEAP "pyspark.StorageLevel.OFF_HEAP") |   
[`TaskContext.attemptNumber`](api/pyspark.TaskContext.attemptNumber.html#pyspark.TaskContext.attemptNumber "pyspark.TaskContext.attemptNumber")() | How many times this task has been attempted.  
[`TaskContext.cpus`](api/pyspark.TaskContext.cpus.html#pyspark.TaskContext.cpus "pyspark.TaskContext.cpus")() | CPUs allocated to the task.  
[`TaskContext.get`](api/pyspark.TaskContext.get.html#pyspark.TaskContext.get "pyspark.TaskContext.get")() | Return the currently active [`TaskContext`](api/pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext").  
[`TaskContext.getLocalProperty`](api/pyspark.TaskContext.getLocalProperty.html#pyspark.TaskContext.getLocalProperty "pyspark.TaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`TaskContext.partitionId`](api/pyspark.TaskContext.partitionId.html#pyspark.TaskContext.partitionId "pyspark.TaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`TaskContext.resources`](api/pyspark.TaskContext.resources.html#pyspark.TaskContext.resources "pyspark.TaskContext.resources")() | Resources allocated to the task.  
[`TaskContext.stageId`](api/pyspark.TaskContext.stageId.html#pyspark.TaskContext.stageId "pyspark.TaskContext.stageId")() | The ID of the stage that this task belong to.  
[`TaskContext.taskAttemptId`](api/pyspark.TaskContext.taskAttemptId.html#pyspark.TaskContext.taskAttemptId "pyspark.TaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
[`RDDBarrier.mapPartitions`](api/pyspark.RDDBarrier.mapPartitions.html#pyspark.RDDBarrier.mapPartitions "pyspark.RDDBarrier.mapPartitions")(f[,Â ...]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, where tasks are launched together in a barrier stage.  
[`RDDBarrier.mapPartitionsWithIndex`](api/pyspark.RDDBarrier.mapPartitionsWithIndex.html#pyspark.RDDBarrier.mapPartitionsWithIndex "pyspark.RDDBarrier.mapPartitionsWithIndex")(f[,Â ...]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, while tracking the index of the original partition.  
[`BarrierTaskContext.allGather`](api/pyspark.BarrierTaskContext.allGather.html#pyspark.BarrierTaskContext.allGather "pyspark.BarrierTaskContext.allGather")([message]) | This function blocks until all tasks in the same stage have reached this routine.  
[`BarrierTaskContext.attemptNumber`](api/pyspark.BarrierTaskContext.attemptNumber.html#pyspark.BarrierTaskContext.attemptNumber "pyspark.BarrierTaskContext.attemptNumber")() | How many times this task has been attempted.  
[`BarrierTaskContext.barrier`](api/pyspark.BarrierTaskContext.barrier.html#pyspark.BarrierTaskContext.barrier "pyspark.BarrierTaskContext.barrier")() | Sets a global barrier and waits until all tasks in this stage hit this barrier.  
[`BarrierTaskContext.cpus`](api/pyspark.BarrierTaskContext.cpus.html#pyspark.BarrierTaskContext.cpus "pyspark.BarrierTaskContext.cpus")() | CPUs allocated to the task.  
[`BarrierTaskContext.get`](api/pyspark.BarrierTaskContext.get.html#pyspark.BarrierTaskContext.get "pyspark.BarrierTaskContext.get")() | Return the currently active [`BarrierTaskContext`](api/pyspark.BarrierTaskContext.html#pyspark.BarrierTaskContext "pyspark.BarrierTaskContext").  
[`BarrierTaskContext.getLocalProperty`](api/pyspark.BarrierTaskContext.getLocalProperty.html#pyspark.BarrierTaskContext.getLocalProperty "pyspark.BarrierTaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`BarrierTaskContext.getTaskInfos`](api/pyspark.BarrierTaskContext.getTaskInfos.html#pyspark.BarrierTaskContext.getTaskInfos "pyspark.BarrierTaskContext.getTaskInfos")() | Returns [`BarrierTaskInfo`](api/pyspark.BarrierTaskInfo.html#pyspark.BarrierTaskInfo "pyspark.BarrierTaskInfo") for all tasks in this barrier stage, ordered by partition ID.  
[`BarrierTaskContext.partitionId`](api/pyspark.BarrierTaskContext.partitionId.html#pyspark.BarrierTaskContext.partitionId "pyspark.BarrierTaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`BarrierTaskContext.resources`](api/pyspark.BarrierTaskContext.resources.html#pyspark.BarrierTaskContext.resources "pyspark.BarrierTaskContext.resources")() | Resources allocated to the task.  
[`BarrierTaskContext.stageId`](api/pyspark.BarrierTaskContext.stageId.html#pyspark.BarrierTaskContext.stageId "pyspark.BarrierTaskContext.stageId")() | The ID of the stage that this task belong to.  
[`BarrierTaskContext.taskAttemptId`](api/pyspark.BarrierTaskContext.taskAttemptId.html#pyspark.BarrierTaskContext.taskAttemptId "pyspark.BarrierTaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](api/pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
[`util.VersionUtils.majorMinorVersion`](api/pyspark.util.VersionUtils.majorMinorVersion.html#pyspark.util.VersionUtils.majorMinorVersion "pyspark.util.VersionUtils.majorMinorVersion")(sparkVersion) | Given a Spark version string, return the (major version number, minor version number).  
  
__On this page

[ __Show Source](../_sources/reference/pyspark.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html

# pyspark.SparkContext#

_class _pyspark.SparkContext(_master=None_ , _appName=None_ , _sparkHome=None_ , _pyFiles=None_ , _environment=None_ , _batchSize=0_ , _serializer=CloudPickleSerializer()_ , _conf=None_ , _gateway=None_ , _jsc=None_ , _profiler_cls= <class 'pyspark.profiler.BasicProfiler'>_, _udf_profiler_cls= <class 'pyspark.profiler.UDFBasicProfiler'>_, _memory_profiler_cls= <class 'pyspark.profiler.MemoryProfiler'>_)[[source]](../../_modules/pyspark/core/context.html#SparkContext)#
    

Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, and can be used to create [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") and broadcast variables on that cluster.

When you create a new SparkContext, at least the master and app name should be set, either through the named parameters here or through conf.

Parameters
    

**master** str, optional
    

Cluster URL to connect to (e.g. spark://host:port, local[4]).

**appName** str, optional
    

A name for your job, to display on the cluster web UI.

**sparkHome** str, optional
    

Location where Spark is installed on cluster nodes.

**pyFiles** list, optional
    

Collection of .zip or .py files to send to the cluster and add to PYTHONPATH. These can be paths on the local file system or HDFS, HTTP, HTTPS, or FTP URLs.

**environment** dict, optional
    

A dictionary of environment variables to set on worker nodes.

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. Set 1 to disable batching, 0 to automatically choose the batch size based on object sizes, or -1 to use an unlimited batch size

**serializer**` Serializer`, optional, default `CPickleSerializer`
    

The serializer for RDDs.

**conf**[` SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf"), optional
    

An object setting Spark properties.

**gateway** class:py4j.java_gateway.JavaGateway, optional
    

Use an existing gateway and JVM, otherwise a new JVM will be instantiated. This is only used internally.

**jsc** class:py4j.java_gateway.JavaObject, optional
    

The JavaSparkContext instance. This is only used internally.

**profiler_cls** type, optional, default `BasicProfiler`
    

A class of custom Profiler used to do profiling

**udf_profiler_cls** type, optional, default `UDFBasicProfiler`
    

A class of custom Profiler used to do udf profiling

Notes

Only one `SparkContext` should be active per JVM. You must stop() the active `SparkContext` before creating a new one.

`SparkContext` instance is not supported to share across multiple processes out of the box, and PySpark does not guarantee multi-processing execution. Use threads instead for concurrent processing purpose.

Examples
    
    
    >>> from pyspark.core.context import SparkContext
    >>> sc = SparkContext('local', 'test')
    >>> sc2 = SparkContext('local', 'test2') 
    Traceback (most recent call last):
        ...
    ValueError: ...
    

Methods

[`accumulator`](pyspark.SparkContext.accumulator.html#pyspark.SparkContext.accumulator "pyspark.SparkContext.accumulator")(value[,Â accum_param]) | Create an [`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator") with the given initial value, using a given [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") helper object to define how to add values of the data type if provided.  
---|---  
[`addArchive`](pyspark.SparkContext.addArchive.html#pyspark.SparkContext.addArchive "pyspark.SparkContext.addArchive")(path) | Add an archive to be downloaded with this Spark job on every node.  
[`addFile`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")(path[,Â recursive]) | Add a file to be downloaded with this Spark job on every node.  
[`addJobTag`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")(tag) | Add a tag to be assigned to all the jobs started by this thread.  
[`addPyFile`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")(path) | Add a .py or .zip dependency for all tasks to be executed on this SparkContext in the future.  
[`binaryFiles`](pyspark.SparkContext.binaryFiles.html#pyspark.SparkContext.binaryFiles "pyspark.SparkContext.binaryFiles")(path[,Â minPartitions]) | Read a directory of binary files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI as a byte array.  
[`binaryRecords`](pyspark.SparkContext.binaryRecords.html#pyspark.SparkContext.binaryRecords "pyspark.SparkContext.binaryRecords")(path,Â recordLength) | Load data from a flat binary file, assuming each record is a set of numbers with the specified numerical format (see ByteBuffer), and the number of bytes per record is constant.  
[`broadcast`](pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast")(value) | Broadcast a read-only variable to the cluster, returning a [`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object for reading it in distributed functions.  
[`cancelAllJobs`](pyspark.SparkContext.cancelAllJobs.html#pyspark.SparkContext.cancelAllJobs "pyspark.SparkContext.cancelAllJobs")() | Cancel all jobs that have been scheduled or are running.  
[`cancelJobGroup`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")(groupId) | Cancel active jobs for the specified group.  
[`cancelJobsWithTag`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")(tag) | Cancel active jobs that have the specified tag.  
[`clearJobTags`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")() | Clear the current thread's job tags.  
[`dump_profiles`](pyspark.SparkContext.dump_profiles.html#pyspark.SparkContext.dump_profiles "pyspark.SparkContext.dump_profiles")(path) | Dump the profile stats into directory path  
[`emptyRDD`](pyspark.SparkContext.emptyRDD.html#pyspark.SparkContext.emptyRDD "pyspark.SparkContext.emptyRDD")() | Create an [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that has no partitions or elements.  
[`getCheckpointDir`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")() | Return the directory where RDDs are checkpointed.  
[`getConf`](pyspark.SparkContext.getConf.html#pyspark.SparkContext.getConf "pyspark.SparkContext.getConf")() | Return a copy of this SparkContext's configuration [`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf").  
[`getJobTags`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")() | Get the tags that are currently set to be assigned to all the jobs started by this thread.  
[`getLocalProperty`](pyspark.SparkContext.getLocalProperty.html#pyspark.SparkContext.getLocalProperty "pyspark.SparkContext.getLocalProperty")(key) | Get a local property set in this thread, or null if it is missing.  
[`getOrCreate`](pyspark.SparkContext.getOrCreate.html#pyspark.SparkContext.getOrCreate "pyspark.SparkContext.getOrCreate")([conf]) | Get or instantiate a `SparkContext` and register it as a singleton object.  
[`getSystemProperty`](pyspark.SparkContext.getSystemProperty.html#pyspark.SparkContext.getSystemProperty "pyspark.SparkContext.getSystemProperty")(key) | Get a Java system property, such as java.home.  
[`hadoopFile`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")(path,Â inputFormatClass,Â keyClass,Â ...) | Read an 'old' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`hadoopRDD`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")(inputFormatClass,Â keyClass,Â valueClass) | Read an 'old' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`newAPIHadoopFile`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")(path,Â inputFormatClass,Â ...) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`newAPIHadoopRDD`](pyspark.SparkContext.newAPIHadoopRDD.html#pyspark.SparkContext.newAPIHadoopRDD "pyspark.SparkContext.newAPIHadoopRDD")(inputFormatClass,Â keyClass,Â ...) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`parallelize`](pyspark.SparkContext.parallelize.html#pyspark.SparkContext.parallelize "pyspark.SparkContext.parallelize")(c[,Â numSlices]) | Distribute a local Python collection to form an RDD.  
[`pickleFile`](pyspark.SparkContext.pickleFile.html#pyspark.SparkContext.pickleFile "pyspark.SparkContext.pickleFile")(name[,Â minPartitions]) | Load an RDD previously saved using [`RDD.saveAsPickleFile()`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile") method.  
[`range`](pyspark.SparkContext.range.html#pyspark.SparkContext.range "pyspark.SparkContext.range")(start[,Â end,Â step,Â numSlices]) | Create a new RDD of int containing elements from start to end (exclusive), increased by step every element.  
[`removeJobTag`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")(tag) | Remove a tag previously added to be assigned to all the jobs started by this thread.  
[`runJob`](pyspark.SparkContext.runJob.html#pyspark.SparkContext.runJob "pyspark.SparkContext.runJob")(rdd,Â partitionFunc[,Â partitions,Â ...]) | Executes the given partitionFunc on the specified set of partitions, returning the result as an array of elements.  
[`sequenceFile`](pyspark.SparkContext.sequenceFile.html#pyspark.SparkContext.sequenceFile "pyspark.SparkContext.sequenceFile")(path[,Â keyClass,Â valueClass,Â ...]) | Read a Hadoop SequenceFile with arbitrary key and value Writable class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`setCheckpointDir`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")(dirName) | Set the directory under which RDDs are going to be checkpointed.  
[`setInterruptOnCancel`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")(interruptOnCancel) | Set the behavior of job cancellation from jobs started in this thread.  
[`setJobDescription`](pyspark.SparkContext.setJobDescription.html#pyspark.SparkContext.setJobDescription "pyspark.SparkContext.setJobDescription")(value) | Set a human readable description of the current job.  
[`setJobGroup`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")(groupId,Â description[,Â ...]) | Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.  
[`setLocalProperty`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty")(key,Â value) | Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.  
[`setLogLevel`](pyspark.SparkContext.setLogLevel.html#pyspark.SparkContext.setLogLevel "pyspark.SparkContext.setLogLevel")(logLevel) | Control our logLevel.  
[`setSystemProperty`](pyspark.SparkContext.setSystemProperty.html#pyspark.SparkContext.setSystemProperty "pyspark.SparkContext.setSystemProperty")(key,Â value) | Set a Java system property, such as spark.executor.memory.  
[`show_profiles`](pyspark.SparkContext.show_profiles.html#pyspark.SparkContext.show_profiles "pyspark.SparkContext.show_profiles")() | Print the profile stats to stdout  
[`sparkUser`](pyspark.SparkContext.sparkUser.html#pyspark.SparkContext.sparkUser "pyspark.SparkContext.sparkUser")() | Get SPARK_USER for user who is running SparkContext.  
[`statusTracker`](pyspark.SparkContext.statusTracker.html#pyspark.SparkContext.statusTracker "pyspark.SparkContext.statusTracker")() | Return `StatusTracker` object  
[`stop`](pyspark.SparkContext.stop.html#pyspark.SparkContext.stop "pyspark.SparkContext.stop")() | Shut down the `SparkContext`.  
[`textFile`](pyspark.SparkContext.textFile.html#pyspark.SparkContext.textFile "pyspark.SparkContext.textFile")(name[,Â minPartitions,Â use_unicode]) | Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings.  
[`union`](pyspark.SparkContext.union.html#pyspark.SparkContext.union "pyspark.SparkContext.union")(rdds) | Build the union of a list of RDDs.  
[`wholeTextFiles`](pyspark.SparkContext.wholeTextFiles.html#pyspark.SparkContext.wholeTextFiles "pyspark.SparkContext.wholeTextFiles")(path[,Â minPartitions,Â ...]) | Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
  
Attributes

[`PACKAGE_EXTENSIONS`](pyspark.SparkContext.PACKAGE_EXTENSIONS.html#pyspark.SparkContext.PACKAGE_EXTENSIONS "pyspark.SparkContext.PACKAGE_EXTENSIONS") |   
---|---  
[`applicationId`](pyspark.SparkContext.applicationId.html#pyspark.SparkContext.applicationId "pyspark.SparkContext.applicationId") | A unique identifier for the Spark application.  
[`defaultMinPartitions`](pyspark.SparkContext.defaultMinPartitions.html#pyspark.SparkContext.defaultMinPartitions "pyspark.SparkContext.defaultMinPartitions") | Default min number of partitions for Hadoop RDDs when not given by user  
[`defaultParallelism`](pyspark.SparkContext.defaultParallelism.html#pyspark.SparkContext.defaultParallelism "pyspark.SparkContext.defaultParallelism") | Default level of parallelism to use when not given by user (e.g.  
[`listArchives`](pyspark.SparkContext.listArchives.html#pyspark.SparkContext.listArchives "pyspark.SparkContext.listArchives") | Returns a list of archive paths that are added to resources.  
[`listFiles`](pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles") | Returns a list of file paths that are added to resources.  
[`resources`](pyspark.SparkContext.resources.html#pyspark.SparkContext.resources "pyspark.SparkContext.resources") | Return the resource information of this `SparkContext`.  
[`startTime`](pyspark.SparkContext.startTime.html#pyspark.SparkContext.startTime "pyspark.SparkContext.startTime") | Return the epoch time when the `SparkContext` was started.  
[`uiWebUrl`](pyspark.SparkContext.uiWebUrl.html#pyspark.SparkContext.uiWebUrl "pyspark.SparkContext.uiWebUrl") | Return the URL of the SparkUI instance started by this `SparkContext`  
[`version`](pyspark.SparkContext.version.html#pyspark.SparkContext.version "pyspark.SparkContext.version") | The version of Spark on which this application is running.  
`serializer` |   
`profiler_collector` |   
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html

# pyspark.RDD#

_class _pyspark.RDD(_jrdd_ , _ctx_ , _jrdd_deserializer =AutoBatchedSerializer(CloudPickleSerializer())_)[[source]](../../_modules/pyspark/core/rdd.html#RDD)#
    

A Resilient Distributed Dataset (RDD), the basic abstraction in Spark. Represents an immutable, partitioned collection of elements that can be operated on in parallel.

Methods

[`aggregate`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")(zeroValue,Â seqOp,Â combOp) | Aggregate the elements of each partition, and then the results for all the partitions, using a given combine functions and a neutral "zero value."  
---|---  
[`aggregateByKey`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")(zeroValue,Â seqFunc,Â combFunc) | Aggregate the values of each key, using given combine functions and a neutral "zero value".  
[`barrier`](pyspark.RDD.barrier.html#pyspark.RDD.barrier "pyspark.RDD.barrier")() | Marks the current stage as a barrier stage, where Spark must launch all tasks together.  
[`cache`](pyspark.RDD.cache.html#pyspark.RDD.cache "pyspark.RDD.cache")() | Persist this RDD with the default storage level (MEMORY_ONLY).  
[`cartesian`](pyspark.RDD.cartesian.html#pyspark.RDD.cartesian "pyspark.RDD.cartesian")(other) | Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements `(a, b)` where `a` is in self and `b` is in other.  
[`checkpoint`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")() | Mark this RDD for checkpointing.  
[`cleanShuffleDependencies`](pyspark.RDD.cleanShuffleDependencies.html#pyspark.RDD.cleanShuffleDependencies "pyspark.RDD.cleanShuffleDependencies")([blocking]) | Removes an RDD's shuffles and it's non-persisted ancestors.  
[`coalesce`](pyspark.RDD.coalesce.html#pyspark.RDD.coalesce "pyspark.RDD.coalesce")(numPartitions[,Â shuffle]) | Return a new RDD that is reduced into numPartitions partitions.  
[`cogroup`](pyspark.RDD.cogroup.html#pyspark.RDD.cogroup "pyspark.RDD.cogroup")(other[,Â numPartitions]) | For each key k in self or other, return a resulting RDD that contains a tuple with the list of values for that key in self as well as other.  
[`collect`](pyspark.RDD.collect.html#pyspark.RDD.collect "pyspark.RDD.collect")() | Return a list that contains all the elements in this RDD.  
[`collectAsMap`](pyspark.RDD.collectAsMap.html#pyspark.RDD.collectAsMap "pyspark.RDD.collectAsMap")() | Return the key-value pairs in this RDD to the master as a dictionary.  
[`collectWithJobGroup`](pyspark.RDD.collectWithJobGroup.html#pyspark.RDD.collectWithJobGroup "pyspark.RDD.collectWithJobGroup")(groupId,Â description[,Â ...]) | When collect rdd, use this method to specify job group.  
[`combineByKey`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")(createCombiner,Â mergeValue,Â ...) | Generic function to combine the elements for each key using a custom set of aggregation functions.  
[`count`](pyspark.RDD.count.html#pyspark.RDD.count "pyspark.RDD.count")() | Return the number of elements in this RDD.  
[`countApprox`](pyspark.RDD.countApprox.html#pyspark.RDD.countApprox "pyspark.RDD.countApprox")(timeout[,Â confidence]) | Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.  
[`countApproxDistinct`](pyspark.RDD.countApproxDistinct.html#pyspark.RDD.countApproxDistinct "pyspark.RDD.countApproxDistinct")([relativeSD]) | Return approximate number of distinct elements in the RDD.  
[`countByKey`](pyspark.RDD.countByKey.html#pyspark.RDD.countByKey "pyspark.RDD.countByKey")() | Count the number of elements for each key, and return the result to the master as a dictionary.  
[`countByValue`](pyspark.RDD.countByValue.html#pyspark.RDD.countByValue "pyspark.RDD.countByValue")() | Return the count of each unique value in this RDD as a dictionary of (value, count) pairs.  
[`distinct`](pyspark.RDD.distinct.html#pyspark.RDD.distinct "pyspark.RDD.distinct")([numPartitions]) | Return a new RDD containing the distinct elements in this RDD.  
[`filter`](pyspark.RDD.filter.html#pyspark.RDD.filter "pyspark.RDD.filter")(f) | Return a new RDD containing only the elements that satisfy a predicate.  
[`first`](pyspark.RDD.first.html#pyspark.RDD.first "pyspark.RDD.first")() | Return the first element in this RDD.  
[`flatMap`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")(f[,Â preservesPartitioning]) | Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  
[`flatMapValues`](pyspark.RDD.flatMapValues.html#pyspark.RDD.flatMapValues "pyspark.RDD.flatMapValues")(f) | Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDD's partitioning.  
[`fold`](pyspark.RDD.fold.html#pyspark.RDD.fold "pyspark.RDD.fold")(zeroValue,Â op) | Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value."  
[`foldByKey`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")(zeroValue,Â func[,Â numPartitions,Â ...]) | Merge the values for each key using an associative function "func" and a neutral "zeroValue" which may be added to the result an arbitrary number of times, and must not change the result (e.g., 0 for addition, or 1 for multiplication.).  
[`foreach`](pyspark.RDD.foreach.html#pyspark.RDD.foreach "pyspark.RDD.foreach")(f) | Applies a function to all elements of this RDD.  
[`foreachPartition`](pyspark.RDD.foreachPartition.html#pyspark.RDD.foreachPartition "pyspark.RDD.foreachPartition")(f) | Applies a function to each partition of this RDD.  
[`fullOuterJoin`](pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`getCheckpointFile`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")() | Gets the name of the file to which this RDD was checkpointed  
[`getNumPartitions`](pyspark.RDD.getNumPartitions.html#pyspark.RDD.getNumPartitions "pyspark.RDD.getNumPartitions")() | Returns the number of partitions in RDD  
[`getResourceProfile`](pyspark.RDD.getResourceProfile.html#pyspark.RDD.getResourceProfile "pyspark.RDD.getResourceProfile")() | Get the [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") specified with this RDD or None if it wasn't specified.  
[`getStorageLevel`](pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")() | Get the RDD's current storage level.  
[`glom`](pyspark.RDD.glom.html#pyspark.RDD.glom "pyspark.RDD.glom")() | Return an RDD created by coalescing all elements within each partition into a list.  
[`groupBy`](pyspark.RDD.groupBy.html#pyspark.RDD.groupBy "pyspark.RDD.groupBy")(f[,Â numPartitions,Â partitionFunc]) | Return an RDD of grouped items.  
[`groupByKey`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")([numPartitions,Â partitionFunc]) | Group the values for each key in the RDD into a single sequence.  
[`groupWith`](pyspark.RDD.groupWith.html#pyspark.RDD.groupWith "pyspark.RDD.groupWith")(other,Â *others) | Alias for cogroup but with support for multiple RDDs.  
[`histogram`](pyspark.RDD.histogram.html#pyspark.RDD.histogram "pyspark.RDD.histogram")(buckets) | Compute a histogram using the provided buckets.  
[`id`](pyspark.RDD.id.html#pyspark.RDD.id "pyspark.RDD.id")() | A unique ID for this RDD (within its SparkContext).  
[`intersection`](pyspark.RDD.intersection.html#pyspark.RDD.intersection "pyspark.RDD.intersection")(other) | Return the intersection of this RDD and another one.  
[`isCheckpointed`](pyspark.RDD.isCheckpointed.html#pyspark.RDD.isCheckpointed "pyspark.RDD.isCheckpointed")() | Return whether this RDD is checkpointed and materialized, either reliably or locally.  
[`isEmpty`](pyspark.RDD.isEmpty.html#pyspark.RDD.isEmpty "pyspark.RDD.isEmpty")() | Returns true if and only if the RDD contains no elements at all.  
[`isLocallyCheckpointed`](pyspark.RDD.isLocallyCheckpointed.html#pyspark.RDD.isLocallyCheckpointed "pyspark.RDD.isLocallyCheckpointed")() | Return whether this RDD is marked for local checkpointing.  
[`join`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")(other[,Â numPartitions]) | Return an RDD containing all pairs of elements with matching keys in self and other.  
[`keyBy`](pyspark.RDD.keyBy.html#pyspark.RDD.keyBy "pyspark.RDD.keyBy")(f) | Creates tuples of the elements in this RDD by applying f.  
[`keys`](pyspark.RDD.keys.html#pyspark.RDD.keys "pyspark.RDD.keys")() | Return an RDD with the keys of each tuple.  
[`leftOuterJoin`](pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")(other[,Â numPartitions]) | Perform a left outer join of self and other.  
[`localCheckpoint`](pyspark.RDD.localCheckpoint.html#pyspark.RDD.localCheckpoint "pyspark.RDD.localCheckpoint")() | Mark this RDD for local checkpointing using Spark's existing caching layer.  
[`lookup`](pyspark.RDD.lookup.html#pyspark.RDD.lookup "pyspark.RDD.lookup")(key) | Return the list of values in the RDD for key key.  
[`map`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each element of this RDD.  
[`mapPartitions`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each partition of this RDD.  
[`mapPartitionsWithIndex`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`mapPartitionsWithSplit`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`mapValues`](pyspark.RDD.mapValues.html#pyspark.RDD.mapValues "pyspark.RDD.mapValues")(f) | Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD's partitioning.  
[`max`](pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")([key]) | Find the maximum item in this RDD.  
[`mean`](pyspark.RDD.mean.html#pyspark.RDD.mean "pyspark.RDD.mean")() | Compute the mean of this RDD's elements.  
[`meanApprox`](pyspark.RDD.meanApprox.html#pyspark.RDD.meanApprox "pyspark.RDD.meanApprox")(timeout[,Â confidence]) | Approximate operation to return the mean within a timeout or meet the confidence.  
[`min`](pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")([key]) | Find the minimum item in this RDD.  
[`name`](pyspark.RDD.name.html#pyspark.RDD.name "pyspark.RDD.name")() | Return the name of this RDD.  
[`partitionBy`](pyspark.RDD.partitionBy.html#pyspark.RDD.partitionBy "pyspark.RDD.partitionBy")(numPartitions[,Â partitionFunc]) | Return a copy of the RDD partitioned using the specified partitioner.  
[`persist`](pyspark.RDD.persist.html#pyspark.RDD.persist "pyspark.RDD.persist")([storageLevel]) | Set this RDD's storage level to persist its values across operations after the first time it is computed.  
[`pipe`](pyspark.RDD.pipe.html#pyspark.RDD.pipe "pyspark.RDD.pipe")(command[,Â env,Â checkCode]) | Return an RDD created by piping elements to a forked external process.  
[`randomSplit`](pyspark.RDD.randomSplit.html#pyspark.RDD.randomSplit "pyspark.RDD.randomSplit")(weights[,Â seed]) | Randomly splits this RDD with the provided weights.  
[`reduce`](pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")(f) | Reduces the elements of this RDD using the specified commutative and associative binary operator.  
[`reduceByKey`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")(func[,Â numPartitions,Â partitionFunc]) | Merge the values for each key using an associative and commutative reduce function.  
[`reduceByKeyLocally`](pyspark.RDD.reduceByKeyLocally.html#pyspark.RDD.reduceByKeyLocally "pyspark.RDD.reduceByKeyLocally")(func) | Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a dictionary.  
[`repartition`](pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")(numPartitions) | Return a new RDD that has exactly numPartitions partitions.  
[`repartitionAndSortWithinPartitions`](pyspark.RDD.repartitionAndSortWithinPartitions.html#pyspark.RDD.repartitionAndSortWithinPartitions "pyspark.RDD.repartitionAndSortWithinPartitions")([...]) | Repartition the RDD according to the given partitioner and, within each resulting partition, sort records by their keys.  
[`rightOuterJoin`](pyspark.RDD.rightOuterJoin.html#pyspark.RDD.rightOuterJoin "pyspark.RDD.rightOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`sample`](pyspark.RDD.sample.html#pyspark.RDD.sample "pyspark.RDD.sample")(withReplacement,Â fraction[,Â seed]) | Return a sampled subset of this RDD.  
[`sampleByKey`](pyspark.RDD.sampleByKey.html#pyspark.RDD.sampleByKey "pyspark.RDD.sampleByKey")(withReplacement,Â fractions[,Â seed]) | Return a subset of this RDD sampled by key (via stratified sampling).  
[`sampleStdev`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")() | Compute the sample standard deviation of this RDD's elements (which corrects for bias in estimating the standard deviation by dividing by N-1 instead of N).  
[`sampleVariance`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")() | Compute the sample variance of this RDD's elements (which corrects for bias in estimating the variance by dividing by N-1 instead of N).  
[`saveAsHadoopDataset`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")(conf[,Â keyConverter,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`saveAsHadoopFile`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")(path,Â outputFormatClass[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`saveAsNewAPIHadoopDataset`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")(conf[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`saveAsNewAPIHadoopFile`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")(path,Â outputFormatClass) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`saveAsPickleFile`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile")(path[,Â batchSize]) | Save this RDD as a SequenceFile of serialized objects.  
[`saveAsSequenceFile`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")(path[,Â compressionCodecClass]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the "org.apache.hadoop.io.Writable" types that we convert from the RDD's key and value types.  
[`saveAsTextFile`](pyspark.RDD.saveAsTextFile.html#pyspark.RDD.saveAsTextFile "pyspark.RDD.saveAsTextFile")(path[,Â compressionCodecClass]) | Save this RDD as a text file, using string representations of elements.  
[`setName`](pyspark.RDD.setName.html#pyspark.RDD.setName "pyspark.RDD.setName")(name) | Assign a name to this RDD.  
[`sortBy`](pyspark.RDD.sortBy.html#pyspark.RDD.sortBy "pyspark.RDD.sortBy")(keyfunc[,Â ascending,Â numPartitions]) | Sorts this RDD by the given keyfunc  
[`sortByKey`](pyspark.RDD.sortByKey.html#pyspark.RDD.sortByKey "pyspark.RDD.sortByKey")([ascending,Â numPartitions,Â keyfunc]) | Sorts this RDD, which is assumed to consist of (key, value) pairs.  
[`stats`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")() | Return a `StatCounter` object that captures the mean, variance and count of the RDD's elements in one operation.  
[`stdev`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")() | Compute the standard deviation of this RDD's elements.  
[`subtract`](pyspark.RDD.subtract.html#pyspark.RDD.subtract "pyspark.RDD.subtract")(other[,Â numPartitions]) | Return each value in self that is not contained in other.  
[`subtractByKey`](pyspark.RDD.subtractByKey.html#pyspark.RDD.subtractByKey "pyspark.RDD.subtractByKey")(other[,Â numPartitions]) | Return each (key, value) pair in self that has no pair with matching key in other.  
[`sum`](pyspark.RDD.sum.html#pyspark.RDD.sum "pyspark.RDD.sum")() | Add up the elements in this RDD.  
[`sumApprox`](pyspark.RDD.sumApprox.html#pyspark.RDD.sumApprox "pyspark.RDD.sumApprox")(timeout[,Â confidence]) | Approximate operation to return the sum within a timeout or meet the confidence.  
[`take`](pyspark.RDD.take.html#pyspark.RDD.take "pyspark.RDD.take")(num) | Take the first num elements of the RDD.  
[`takeOrdered`](pyspark.RDD.takeOrdered.html#pyspark.RDD.takeOrdered "pyspark.RDD.takeOrdered")(num[,Â key]) | Get the N elements from an RDD ordered in ascending order or as specified by the optional key function.  
[`takeSample`](pyspark.RDD.takeSample.html#pyspark.RDD.takeSample "pyspark.RDD.takeSample")(withReplacement,Â num[,Â seed]) | Return a fixed-size sampled subset of this RDD.  
`toDF`([schema,Â sampleRatio]) |   
[`toDebugString`](pyspark.RDD.toDebugString.html#pyspark.RDD.toDebugString "pyspark.RDD.toDebugString")() | A description of this RDD and its recursive dependencies for debugging.  
[`toLocalIterator`](pyspark.RDD.toLocalIterator.html#pyspark.RDD.toLocalIterator "pyspark.RDD.toLocalIterator")([prefetchPartitions]) | Return an iterator that contains all of the elements in this RDD.  
[`top`](pyspark.RDD.top.html#pyspark.RDD.top "pyspark.RDD.top")(num[,Â key]) | Get the top N elements from an RDD.  
[`treeAggregate`](pyspark.RDD.treeAggregate.html#pyspark.RDD.treeAggregate "pyspark.RDD.treeAggregate")(zeroValue,Â seqOp,Â combOp[,Â depth]) | Aggregates the elements of this RDD in a multi-level tree pattern.  
[`treeReduce`](pyspark.RDD.treeReduce.html#pyspark.RDD.treeReduce "pyspark.RDD.treeReduce")(f[,Â depth]) | Reduces the elements of this RDD in a multi-level tree pattern.  
[`union`](pyspark.RDD.union.html#pyspark.RDD.union "pyspark.RDD.union")(other) | Return the union of this RDD and another one.  
[`unpersist`](pyspark.RDD.unpersist.html#pyspark.RDD.unpersist "pyspark.RDD.unpersist")([blocking]) | Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  
[`values`](pyspark.RDD.values.html#pyspark.RDD.values "pyspark.RDD.values")() | Return an RDD with the values of each tuple.  
[`variance`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")() | Compute the variance of this RDD's elements.  
[`withResources`](pyspark.RDD.withResources.html#pyspark.RDD.withResources "pyspark.RDD.withResources")(profile) | Specify a [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") to use when calculating this RDD.  
[`zip`](pyspark.RDD.zip.html#pyspark.RDD.zip "pyspark.RDD.zip")(other) | Zips this RDD with another one, returning key-value pairs with the first element in each RDD second element in each RDD, etc.  
[`zipWithIndex`](pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex")() | Zips this RDD with its element indices.  
[`zipWithUniqueId`](pyspark.RDD.zipWithUniqueId.html#pyspark.RDD.zipWithUniqueId "pyspark.RDD.zipWithUniqueId")() | Zips this RDD with generated unique Long ids.  
  
Attributes

[`context`](pyspark.RDD.context.html#pyspark.RDD.context "pyspark.RDD.context") | The [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") that this RDD was created on.  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.RDD.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.html

# pyspark.Broadcast#

_class _pyspark.Broadcast(_sc =None_, _value =None_, _pickle_registry =None_, _path =None_, _sock_file =None_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast)#
    

A broadcast variable created with [`SparkContext.broadcast()`](pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast"). Access its value through [`value`](pyspark.Broadcast.value.html#pyspark.Broadcast.value "pyspark.Broadcast.value").

Examples
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    >>> b.value
    [1, 2, 3, 4, 5]
    >>> spark.sparkContext.parallelize([0, 0]).flatMap(lambda x: b.value).collect()
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    >>> b.unpersist()
    
    
    
    >>> large_broadcast = spark.sparkContext.broadcast(range(10000))
    

Methods

[`destroy`](pyspark.Broadcast.destroy.html#pyspark.Broadcast.destroy "pyspark.Broadcast.destroy")([blocking]) | Destroy all data and metadata related to this broadcast variable.  
---|---  
[`dump`](pyspark.Broadcast.dump.html#pyspark.Broadcast.dump "pyspark.Broadcast.dump")(value,Â f) | Write a pickled representation of value to the open file or socket.  
[`load`](pyspark.Broadcast.load.html#pyspark.Broadcast.load "pyspark.Broadcast.load")(file) | Read a pickled representation of value from the open file or socket.  
[`load_from_path`](pyspark.Broadcast.load_from_path.html#pyspark.Broadcast.load_from_path "pyspark.Broadcast.load_from_path")(path) | Read the pickled representation of an object from the open file and return the reconstituted object hierarchy specified therein.  
[`unpersist`](pyspark.Broadcast.unpersist.html#pyspark.Broadcast.unpersist "pyspark.Broadcast.unpersist")([blocking]) | Delete cached copies of this broadcast on the executors.  
  
Attributes

[`value`](pyspark.Broadcast.value.html#pyspark.Broadcast.value "pyspark.Broadcast.value") | Return the broadcasted value  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Accumulator.html

# pyspark.Accumulator#

_class _pyspark.Accumulator(_aid_ , _value_ , _accum_param_)[[source]](../../_modules/pyspark/accumulators.html#Accumulator)#
    

A shared variable that can be accumulated, i.e., has a commutative and associative âaddâ operation. Worker tasks on a Spark cluster can add values to an Accumulator with the += operator, but only the driver program is allowed to access its value, using value. Updates from the workers get propagated automatically to the driver program.

While [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") supports accumulators for primitive data types like `int` and `float`, users can also define accumulators for custom types by providing a custom [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") object. Refer to its doctest for an example.

Examples
    
    
    >>> a = sc.accumulator(1)
    >>> a.value
    1
    >>> a.value = 2
    >>> a.value
    2
    >>> a += 5
    >>> a.value
    7
    >>> sc.accumulator(1.0).value
    1.0
    >>> sc.accumulator(1j).value
    1j
    >>> rdd = sc.parallelize([1,2,3])
    >>> def f(x):
    ...     global a
    ...     a += x
    ...
    >>> rdd.foreach(f)
    >>> a.value
    13
    >>> b = sc.accumulator(0)
    >>> def g(x):
    ...     b.add(x)
    ...
    >>> rdd.foreach(g)
    >>> b.value
    6
    
    
    
    >>> rdd.map(lambda x: a.value).collect() 
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...
    
    
    
    >>> def h(x):
    ...     global a
    ...     a.value = 7
    ...
    >>> rdd.foreach(h) 
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...
    
    
    
    >>> sc.accumulator([1.0, 2.0, 3.0]) 
    Traceback (most recent call last):
        ...
    TypeError: ...
    

Methods

[`add`](pyspark.Accumulator.add.html#pyspark.Accumulator.add "pyspark.Accumulator.add")(term) | Adds a term to this accumulator's value  
---|---  
  
Attributes

[`value`](pyspark.Accumulator.value.html#pyspark.Accumulator.value "pyspark.Accumulator.value") | Get the accumulator's value; only usable in driver program  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.Accumulator.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.AccumulatorParam.html

# pyspark.AccumulatorParam#

_class _pyspark.AccumulatorParam[[source]](../../_modules/pyspark/accumulators.html#AccumulatorParam)#
    

Helper object that defines how to accumulate values of a given type.

Examples
    
    
    >>> from pyspark.accumulators import AccumulatorParam
    >>> class VectorAccumulatorParam(AccumulatorParam):
    ...     def zero(self, value):
    ...         return [0.0] * len(value)
    ...     def addInPlace(self, val1, val2):
    ...         for i in range(len(val1)):
    ...              val1[i] += val2[i]
    ...         return val1
    >>> va = sc.accumulator([1.0, 2.0, 3.0], VectorAccumulatorParam())
    >>> va.value
    [1.0, 2.0, 3.0]
    >>> def g(x):
    ...     global va
    ...     va += [x] * 3
    ...
    >>> rdd = sc.parallelize([1,2,3])
    >>> rdd.foreach(g)
    >>> va.value
    [7.0, 8.0, 9.0]
    

Methods

[`addInPlace`](pyspark.AccumulatorParam.addInPlace.html#pyspark.AccumulatorParam.addInPlace "pyspark.AccumulatorParam.addInPlace")(value1,Â value2) | Add two values of the accumulator's data type, returning a new value; for efficiency, can also update value1 in place and return it.  
---|---  
[`zero`](pyspark.AccumulatorParam.zero.html#pyspark.AccumulatorParam.zero "pyspark.AccumulatorParam.zero")(value) | Provide a "zero value" for the type, compatible in dimensions with the provided value (e.g., a zero vector)  
  
[ __Show Source](../../_sources/reference/api/pyspark.AccumulatorParam.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html

# pyspark.SparkConf#

_class _pyspark.SparkConf(_loadDefaults =True_, __jvm =None_, __jconf =None_)[[source]](../../_modules/pyspark/conf.html#SparkConf)#
    

Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.

Most of the time, you would create a SparkConf object with `SparkConf()`, which will load values from spark.* Java system properties as well. In this case, any parameters you set directly on the `SparkConf` object take priority over system properties.

For unit tests, you can also call `SparkConf(false)` to skip loading external settings and get the same configuration no matter what the system properties are.

All setter methods in this class support chaining. For example, you can write `conf.setMaster("local").setAppName("My app")`.

Parameters
    

**loadDefaults** bool
    

whether to load values from Java system properties (True by default)

**_jvm** class:py4j.java_gateway.JVMView
    

internal parameter used to pass a handle to the Java VM; does not need to be set by users

**_jconf** class:py4j.java_gateway.JavaObject
    

Optionally pass in an existing SparkConf handle to use its parameters

Notes

Once a SparkConf object is passed to Spark, it is cloned and can no longer be modified by the user.

Examples
    
    
    >>> from pyspark import SparkConf, SparkContext
    >>> conf = SparkConf()
    >>> conf.setMaster("local").setAppName("My app")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.master")
    'local'
    >>> conf.get("spark.app.name")
    'My app'
    >>> sc = SparkContext(conf=conf)
    >>> sc.master
    'local'
    >>> sc.appName
    'My app'
    >>> sc.sparkHome is None
    True
    
    
    
    >>> conf = SparkConf(loadDefaults=False)
    >>> conf.setSparkHome("/path")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.home")
    '/path'
    >>> conf.setExecutorEnv("VAR1", "value1")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.setExecutorEnv(pairs = [("VAR3", "value3"), ("VAR4", "value4")])
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.executorEnv.VAR1")
    'value1'
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.home=/path
    >>> for p in sorted(conf.getAll(), key=lambda p: p[0]):
    ...     print(p)
    ('spark.executorEnv.VAR1', 'value1')
    ('spark.executorEnv.VAR3', 'value3')
    ('spark.executorEnv.VAR4', 'value4')
    ('spark.home', '/path')
    >>> conf._jconf.setExecutorEnv("VAR5", "value5")
    JavaObject id...
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.executorEnv.VAR5=value5
    spark.home=/path
    

Methods

[`contains`](pyspark.SparkConf.contains.html#pyspark.SparkConf.contains "pyspark.SparkConf.contains")(key) | Does this configuration contain a given key?  
---|---  
[`get`](pyspark.SparkConf.get.html#pyspark.SparkConf.get "pyspark.SparkConf.get")(key[,Â defaultValue]) | Get the configured value for some key, or return a default otherwise.  
[`getAll`](pyspark.SparkConf.getAll.html#pyspark.SparkConf.getAll "pyspark.SparkConf.getAll")() | Get all values as a list of key-value pairs.  
[`set`](pyspark.SparkConf.set.html#pyspark.SparkConf.set "pyspark.SparkConf.set")(key,Â value) | Set a configuration property.  
[`setAll`](pyspark.SparkConf.setAll.html#pyspark.SparkConf.setAll "pyspark.SparkConf.setAll")(pairs) | Set multiple parameters, passed as a list of key-value pairs.  
[`setAppName`](pyspark.SparkConf.setAppName.html#pyspark.SparkConf.setAppName "pyspark.SparkConf.setAppName")(value) | Set application name.  
[`setExecutorEnv`](pyspark.SparkConf.setExecutorEnv.html#pyspark.SparkConf.setExecutorEnv "pyspark.SparkConf.setExecutorEnv")([key,Â value,Â pairs]) | Set an environment variable to be passed to executors.  
[`setIfMissing`](pyspark.SparkConf.setIfMissing.html#pyspark.SparkConf.setIfMissing "pyspark.SparkConf.setIfMissing")(key,Â value) | Set a configuration property, if not already set.  
[`setMaster`](pyspark.SparkConf.setMaster.html#pyspark.SparkConf.setMaster "pyspark.SparkConf.setMaster")(value) | Set master URL to connect to.  
[`setSparkHome`](pyspark.SparkConf.setSparkHome.html#pyspark.SparkConf.setSparkHome "pyspark.SparkConf.setSparkHome")(value) | Set path where Spark is installed on worker nodes.  
[`toDebugString`](pyspark.SparkConf.toDebugString.html#pyspark.SparkConf.toDebugString "pyspark.SparkConf.toDebugString")() | Returns a printable version of the configuration, as a list of key=value pairs, one per line.  
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkFiles.html

# pyspark.SparkFiles#

_class _pyspark.SparkFiles[[source]](../../_modules/pyspark/core/files.html#SparkFiles)#
    

Resolves paths to files added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile").

SparkFiles contains only classmethods; users should not create SparkFiles instances.

Methods

[`get`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")(filename) | Get the absolute path of a file added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
---|---  
[`getRootDirectory`](pyspark.SparkFiles.getRootDirectory.html#pyspark.SparkFiles.getRootDirectory "pyspark.SparkFiles.getRootDirectory")() | Get the root directory that contains files added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkFiles.rst.txt)


---

## 🔹 009. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.html

# pyspark.StorageLevel#

_class _pyspark.StorageLevel(_useDisk_ , _useMemory_ , _useOffHeap_ , _deserialized_ , _replication =1_)[[source]](../../_modules/pyspark/storagelevel.html#StorageLevel)#
    

Flags for controlling the storage of an RDD. Each StorageLevel records whether to use memory, whether to drop the RDD to disk if it falls out of memory, whether to keep the data in memory in a JAVA-specific serialized format, and whether to replicate the RDD partitions on multiple nodes. Also contains static constants for some commonly used storage levels, MEMORY_ONLY. Since the data is always serialized on the Python side, all the constants use the serialized formats.

Attributes

[`DISK_ONLY`](pyspark.StorageLevel.DISK_ONLY.html#pyspark.StorageLevel.DISK_ONLY "pyspark.StorageLevel.DISK_ONLY") |   
---|---  
[`DISK_ONLY_2`](pyspark.StorageLevel.DISK_ONLY_2.html#pyspark.StorageLevel.DISK_ONLY_2 "pyspark.StorageLevel.DISK_ONLY_2") |   
[`DISK_ONLY_3`](pyspark.StorageLevel.DISK_ONLY_3.html#pyspark.StorageLevel.DISK_ONLY_3 "pyspark.StorageLevel.DISK_ONLY_3") |   
[`MEMORY_AND_DISK`](pyspark.StorageLevel.MEMORY_AND_DISK.html#pyspark.StorageLevel.MEMORY_AND_DISK "pyspark.StorageLevel.MEMORY_AND_DISK") |   
[`MEMORY_AND_DISK_2`](pyspark.StorageLevel.MEMORY_AND_DISK_2.html#pyspark.StorageLevel.MEMORY_AND_DISK_2 "pyspark.StorageLevel.MEMORY_AND_DISK_2") |   
[`MEMORY_AND_DISK_DESER`](pyspark.StorageLevel.MEMORY_AND_DISK_DESER.html#pyspark.StorageLevel.MEMORY_AND_DISK_DESER "pyspark.StorageLevel.MEMORY_AND_DISK_DESER") |   
[`MEMORY_ONLY`](pyspark.StorageLevel.MEMORY_ONLY.html#pyspark.StorageLevel.MEMORY_ONLY "pyspark.StorageLevel.MEMORY_ONLY") |   
[`MEMORY_ONLY_2`](pyspark.StorageLevel.MEMORY_ONLY_2.html#pyspark.StorageLevel.MEMORY_ONLY_2 "pyspark.StorageLevel.MEMORY_ONLY_2") |   
`NONE` |   
[`OFF_HEAP`](pyspark.StorageLevel.OFF_HEAP.html#pyspark.StorageLevel.OFF_HEAP "pyspark.StorageLevel.OFF_HEAP") |   
  
[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.rst.txt)


---

## 🔹 010. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.html

# pyspark.TaskContext#

_class _pyspark.TaskContext[[source]](../../_modules/pyspark/taskcontext.html#TaskContext)#
    

Contextual information about a task which can be read or mutated during execution. To access the TaskContext for a running task, use: [`TaskContext.get()`](pyspark.TaskContext.get.html#pyspark.TaskContext.get "pyspark.TaskContext.get").

New in version 2.2.0.

Examples
    
    
    >>> from pyspark import TaskContext
    

Get a task context instance from [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD").
    
    
    >>> spark.sparkContext.setLocalProperty("key1", "value")
    >>> taskcontext = spark.sparkContext.parallelize([1]).map(lambda _: TaskContext.get()).first()
    >>> isinstance(taskcontext.attemptNumber(), int)
    True
    >>> isinstance(taskcontext.partitionId(), int)
    True
    >>> isinstance(taskcontext.stageId(), int)
    True
    >>> isinstance(taskcontext.taskAttemptId(), int)
    True
    >>> taskcontext.getLocalProperty("key1")
    'value'
    >>> isinstance(taskcontext.cpus(), int)
    True
    

Get a task context instance from a dataframe via Python UDF.
    
    
    >>> from pyspark.sql import Row
    >>> from pyspark.sql.functions import udf
    >>> @udf("STRUCT<anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row():
    ...    taskcontext = TaskContext.get()
    ...    return Row(
    ...        anum=taskcontext.attemptNumber(),
    ...        partid=taskcontext.partitionId(),
    ...        stageid=taskcontext.stageId(),
    ...        taskaid=taskcontext.taskAttemptId(),
    ...        prop=taskcontext.getLocalProperty("key2"),
    ...        cpus=taskcontext.cpus())
    ...
    >>> spark.sparkContext.setLocalProperty("key2", "value")
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row()).first()
    ... )
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    'value'
    >>> isinstance(cpus, int)
    True
    

Get a task context instance from a dataframe via Pandas UDF.
    
    
    >>> import pandas as pd  
    >>> from pyspark.sql.functions import pandas_udf
    >>> @pandas_udf("STRUCT<"
    ...     "anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row(_):
    ...    taskcontext = TaskContext.get()
    ...    return pd.DataFrame({
    ...        "anum": [taskcontext.attemptNumber()],
    ...        "partid": [taskcontext.partitionId()],
    ...        "stageid": [taskcontext.stageId()],
    ...        "taskaid": [taskcontext.taskAttemptId()],
    ...        "prop": [taskcontext.getLocalProperty("key3")],
    ...        "cpus": [taskcontext.cpus()]
    ...    })  
    ...
    >>> spark.sparkContext.setLocalProperty("key3", "value")  
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row("id")).first()
    ... )  
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    'value'
    >>> isinstance(cpus, int)
    True
    

Methods

[`attemptNumber`](pyspark.TaskContext.attemptNumber.html#pyspark.TaskContext.attemptNumber "pyspark.TaskContext.attemptNumber")() | How many times this task has been attempted.  
---|---  
[`cpus`](pyspark.TaskContext.cpus.html#pyspark.TaskContext.cpus "pyspark.TaskContext.cpus")() | CPUs allocated to the task.  
[`get`](pyspark.TaskContext.get.html#pyspark.TaskContext.get "pyspark.TaskContext.get")() | Return the currently active `TaskContext`.  
[`getLocalProperty`](pyspark.TaskContext.getLocalProperty.html#pyspark.TaskContext.getLocalProperty "pyspark.TaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`partitionId`](pyspark.TaskContext.partitionId.html#pyspark.TaskContext.partitionId "pyspark.TaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`resources`](pyspark.TaskContext.resources.html#pyspark.TaskContext.resources "pyspark.TaskContext.resources")() | Resources allocated to the task.  
[`stageId`](pyspark.TaskContext.stageId.html#pyspark.TaskContext.stageId "pyspark.TaskContext.stageId")() | The ID of the stage that this task belong to.  
[`taskAttemptId`](pyspark.TaskContext.taskAttemptId.html#pyspark.TaskContext.taskAttemptId "pyspark.TaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
  
[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.rst.txt)


---

## 🔹 011. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDDBarrier.html

# pyspark.RDDBarrier#

_class _pyspark.RDDBarrier(_rdd_)[[source]](../../_modules/pyspark/core/rdd.html#RDDBarrier)#
    

Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together. `RDDBarrier` instances are created by [`RDD.barrier()`](pyspark.RDD.barrier.html#pyspark.RDD.barrier "pyspark.RDD.barrier").

New in version 2.4.0.

Notes

This API is experimental

Methods

[`mapPartitions`](pyspark.RDDBarrier.mapPartitions.html#pyspark.RDDBarrier.mapPartitions "pyspark.RDDBarrier.mapPartitions")(f[,Â preservesPartitioning]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, where tasks are launched together in a barrier stage.  
---|---  
[`mapPartitionsWithIndex`](pyspark.RDDBarrier.mapPartitionsWithIndex.html#pyspark.RDDBarrier.mapPartitionsWithIndex "pyspark.RDDBarrier.mapPartitionsWithIndex")(f[,Â ...]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, while tracking the index of the original partition.  
  
[ __Show Source](../../_sources/reference/api/pyspark.RDDBarrier.rst.txt)


---

## 🔹 012. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.html

# pyspark.BarrierTaskContext#

_class _pyspark.BarrierTaskContext[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext)#
    

A [`TaskContext`](pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage. Use [`BarrierTaskContext.get()`](pyspark.BarrierTaskContext.get.html#pyspark.BarrierTaskContext.get "pyspark.BarrierTaskContext.get") to obtain the barrier context for a running barrier task.

New in version 2.4.0.

Notes

This API is experimental

Examples

Set a barrier, and execute it with RDD.
    
    
    >>> from pyspark import BarrierTaskContext
    >>> def block_and_do_something(itr):
    ...     taskcontext = BarrierTaskContext.get()
    ...     # Do something.
    ...
    ...     # Wait until all tasks finished.
    ...     taskcontext.barrier()
    ...
    ...     return itr
    ...
    >>> rdd = spark.sparkContext.parallelize([1])
    >>> rdd.barrier().mapPartitions(block_and_do_something).collect()
    [1]
    

Methods

[`allGather`](pyspark.BarrierTaskContext.allGather.html#pyspark.BarrierTaskContext.allGather "pyspark.BarrierTaskContext.allGather")([message]) | This function blocks until all tasks in the same stage have reached this routine.  
---|---  
[`attemptNumber`](pyspark.BarrierTaskContext.attemptNumber.html#pyspark.BarrierTaskContext.attemptNumber "pyspark.BarrierTaskContext.attemptNumber")() | How many times this task has been attempted.  
[`barrier`](pyspark.BarrierTaskContext.barrier.html#pyspark.BarrierTaskContext.barrier "pyspark.BarrierTaskContext.barrier")() | Sets a global barrier and waits until all tasks in this stage hit this barrier.  
[`cpus`](pyspark.BarrierTaskContext.cpus.html#pyspark.BarrierTaskContext.cpus "pyspark.BarrierTaskContext.cpus")() | CPUs allocated to the task.  
[`get`](pyspark.BarrierTaskContext.get.html#pyspark.BarrierTaskContext.get "pyspark.BarrierTaskContext.get")() | Return the currently active `BarrierTaskContext`.  
[`getLocalProperty`](pyspark.BarrierTaskContext.getLocalProperty.html#pyspark.BarrierTaskContext.getLocalProperty "pyspark.BarrierTaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`getTaskInfos`](pyspark.BarrierTaskContext.getTaskInfos.html#pyspark.BarrierTaskContext.getTaskInfos "pyspark.BarrierTaskContext.getTaskInfos")() | Returns [`BarrierTaskInfo`](pyspark.BarrierTaskInfo.html#pyspark.BarrierTaskInfo "pyspark.BarrierTaskInfo") for all tasks in this barrier stage, ordered by partition ID.  
[`partitionId`](pyspark.BarrierTaskContext.partitionId.html#pyspark.BarrierTaskContext.partitionId "pyspark.BarrierTaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`resources`](pyspark.BarrierTaskContext.resources.html#pyspark.BarrierTaskContext.resources "pyspark.BarrierTaskContext.resources")() | Resources allocated to the task.  
[`stageId`](pyspark.BarrierTaskContext.stageId.html#pyspark.BarrierTaskContext.stageId "pyspark.BarrierTaskContext.stageId")() | The ID of the stage that this task belong to.  
[`taskAttemptId`](pyspark.BarrierTaskContext.taskAttemptId.html#pyspark.BarrierTaskContext.taskAttemptId "pyspark.BarrierTaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
  
[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.rst.txt)


---

## 🔹 013. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskInfo.html

# pyspark.BarrierTaskInfo#

_class _pyspark.BarrierTaskInfo(_address_)[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskInfo)#
    

Carries all task infos of a barrier task.

New in version 2.4.0.

Notes

This API is experimental

Attributes
    

**address** str
    

The IPv4 address (host:port) of the executor that the barrier task is running on

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskInfo.rst.txt)


---

## 🔹 014. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.InheritableThread.html

# pyspark.InheritableThread#

_class _pyspark.InheritableThread(_target_ , _* args_, _session =None_, _** kwargs_)[[source]](../../_modules/pyspark/util.html#InheritableThread)#
    

Thread that is recommended to be used in PySpark when the pinned thread mode is enabled. The wrapper function, before calling original thread target, it inherits the inheritable properties specific to JVM thread such as `InheritableThreadLocal`, or thread local such as tags with Spark Connect.

When the pinned thread mode is off, this works as `threading.Thread`.

New in version 3.1.0.

Changed in version 3.5.0: Supports Spark Connect.

Notes

This API is experimental.

Methods

`getName`() |   
---|---  
`isDaemon`() |   
`is_alive`() | Return whether the thread is alive.  
`join`([timeout]) | Wait until the thread terminates.  
`run`() | Method representing the thread's activity.  
`setDaemon`(daemonic) |   
`setName`(name) |   
`start`() | Start the thread's activity.  
  
Attributes

`daemon` | A boolean value indicating whether this thread is a daemon thread.  
---|---  
`ident` | Thread identifier of this thread or None if it has not been started.  
`name` | A string used for identification purposes only.  
`native_id` | Native integral thread ID of this thread, or None if it has not been started.  
  
[ __Show Source](../../_sources/reference/api/pyspark.InheritableThread.rst.txt)


---

## 🔹 015. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.util.VersionUtils.html

# pyspark.util.VersionUtils#

_class _pyspark.util.VersionUtils[[source]](../../_modules/pyspark/util.html#VersionUtils)#
    

Provides utility method to determine Spark versions with given input string.

Methods

[`majorMinorVersion`](pyspark.util.VersionUtils.majorMinorVersion.html#pyspark.util.VersionUtils.majorMinorVersion "pyspark.util.VersionUtils.majorMinorVersion")(sparkVersion) | Given a Spark version string, return the (major version number, minor version number).  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.util.VersionUtils.rst.txt)


---

## 🔹 016. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.PACKAGE_EXTENSIONS.html

# pyspark.SparkContext.PACKAGE_EXTENSIONS#

SparkContext.PACKAGE_EXTENSIONS _ = ('.zip', '.egg', '.jar')_#
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.PACKAGE_EXTENSIONS.rst.txt)


---

## 🔹 017. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.accumulator.html

# pyspark.SparkContext.accumulator#

SparkContext.accumulator(_value_ , _accum_param =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.accumulator)#
    

Create an [`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator") with the given initial value, using a given [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") helper object to define how to add values of the data type if provided. Default AccumulatorParams are used for integers and floating-point numbers if you do not provide one. For other types, a custom AccumulatorParam can be used.

New in version 0.7.0.

Parameters
    

**value** T
    

initialized value

**accum_param**[` pyspark.AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam"), optional
    

helper object to define how to add values

Returns
    

[`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator")
    

Accumulator object, a shared variable that can be accumulated

Examples
    
    
    >>> acc = sc.accumulator(9)
    >>> acc.value
    9
    >>> acc += 1
    >>> acc.value
    10
    

Accumulator object can be accumulated in RDD operations:
    
    
    >>> rdd = sc.range(5)
    >>> def f(x):
    ...     global acc
    ...     acc += 1
    ...
    >>> rdd.foreach(f)
    >>> acc.value
    15
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.accumulator.rst.txt)


---

## 🔹 018. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addArchive.html

# pyspark.SparkContext.addArchive#

SparkContext.addArchive(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addArchive)#
    

Add an archive to be downloaded with this Spark job on every node. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") with the filename to find its download/unpacked location. The given path should be one of .zip, .tar, .tar.gz, .tgz and .jar.

New in version 3.3.0.

Parameters
    

**path** str
    

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") to find its download location.

See also

[`SparkContext.listArchives()`](pyspark.SparkContext.listArchives.html#pyspark.SparkContext.listArchives "pyspark.SparkContext.listArchives")
    
[`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored. This API is experimental.

Examples

Creates a zipped file that contains a text file written â100â.
    
    
    >>> import os
    >>> import tempfile
    >>> import zipfile
    >>> from pyspark import SparkFiles
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="addArchive") as d:
    ...     path = os.path.join(d, "test.txt")
    ...     with open(path, "w") as f:
    ...         _ = f.write("100")
    ...
    ...     zip_path1 = os.path.join(d, "test1.zip")
    ...     with zipfile.ZipFile(zip_path1, "w", zipfile.ZIP_DEFLATED) as z:
    ...         z.write(path, os.path.basename(path))
    ...
    ...     zip_path2 = os.path.join(d, "test2.zip")
    ...     with zipfile.ZipFile(zip_path2, "w", zipfile.ZIP_DEFLATED) as z:
    ...         z.write(path, os.path.basename(path))
    ...
    ...     sc.addArchive(zip_path1)
    ...     arch_list1 = sorted(sc.listArchives)
    ...
    ...     sc.addArchive(zip_path2)
    ...     arch_list2 = sorted(sc.listArchives)
    ...
    ...     # add zip_path2 twice, this addition will be ignored
    ...     sc.addArchive(zip_path2)
    ...     arch_list3 = sorted(sc.listArchives)
    ...
    ...     def func(iterator):
    ...         with open("%s/test.txt" % SparkFiles.get("test1.zip")) as f:
    ...             mul = int(f.readline())
    ...             return [x * mul for x in iterator]
    ...
    ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()
    
    
    
    >>> arch_list1
    ['file:/.../test1.zip']
    >>> arch_list2
    ['file:/.../test1.zip', 'file:/.../test2.zip']
    >>> arch_list3
    ['file:/.../test1.zip', 'file:/.../test2.zip']
    >>> collected
    [100, 200, 300, 400]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addArchive.rst.txt)


---

## 🔹 019. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addFile.html

# pyspark.SparkContext.addFile#

SparkContext.addFile(_path_ , _recursive =False_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addFile)#
    

Add a file to be downloaded with this Spark job on every node. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") with the filename to find its download location.

A directory can be given if the recursive option is set to True. Currently directories are only supported for Hadoop-supported filesystems.

New in version 0.7.0.

Parameters
    

**path** str
    

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") to find its download location.

**recursive** bool, default False
    

whether to recursively add files in the input directory

See also

[`SparkContext.listFiles()`](pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles")
    
[`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")
    
[`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored.

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> from pyspark import SparkFiles
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="addFile") as d:
    ...     path1 = os.path.join(d, "test1.txt")
    ...     with open(path1, "w") as f:
    ...         _ = f.write("100")
    ...
    ...     path2 = os.path.join(d, "test2.txt")
    ...     with open(path2, "w") as f:
    ...         _ = f.write("200")
    ...
    ...     sc.addFile(path1)
    ...     file_list1 = sorted(sc.listFiles)
    ...
    ...     sc.addFile(path2)
    ...     file_list2 = sorted(sc.listFiles)
    ...
    ...     # add path2 twice, this addition will be ignored
    ...     sc.addFile(path2)
    ...     file_list3 = sorted(sc.listFiles)
    ...
    ...     def func(iterator):
    ...         with open(SparkFiles.get("test1.txt")) as f:
    ...             mul = int(f.readline())
    ...             return [x * mul for x in iterator]
    ...
    ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()
    
    
    
    >>> file_list1
    ['file:/.../test1.txt']
    >>> file_list2
    ['file:/.../test1.txt', 'file:/.../test2.txt']
    >>> file_list3
    ['file:/.../test1.txt', 'file:/.../test2.txt']
    >>> collected
    [100, 200, 300, 400]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addFile.rst.txt)


---

## 🔹 020. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addJobTag.html

# pyspark.SparkContext.addJobTag#

SparkContext.addJobTag(_tag_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addJobTag)#
    

Add a tag to be assigned to all the jobs started by this thread.

Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group tag. The application can use [`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag") to cancel all running executions with this tag.

There may be multiple tags present at the same time, so different parts of application may use different tags to perform cancellation at different levels of granularity.

New in version 3.5.0.

Parameters
    

**tag** str
    

The tag to be added. Cannot contain â,â (comma) character.

See also

[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> import threading
    >>> from time import sleep
    >>> from pyspark import InheritableThread
    >>> sc.setInterruptOnCancel(interruptOnCancel=True)
    >>> result = "Not Set"
    >>> lock = threading.Lock()
    >>> def map_func(x):
    ...     sleep(100)
    ...     raise RuntimeError("Task should have been cancelled")
    ...
    >>> def start_job(x):
    ...     global result
    ...     try:
    ...         sc.addJobTag("job_to_cancel")
    ...         result = sc.parallelize(range(x)).map(map_func).collect()
    ...     except Exception as e:
    ...         result = "Cancelled"
    ...     lock.release()
    ...
    >>> def stop_job():
    ...     sleep(5)
    ...     sc.cancelJobsWithTag("job_to_cancel")
    ...
    >>> suppress = lock.acquire()
    >>> suppress = InheritableThread(target=start_job, args=(10,)).start()
    >>> suppress = InheritableThread(target=stop_job).start()
    >>> suppress = lock.acquire()
    >>> print(result)
    Cancelled
    >>> sc.clearJobTags()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addJobTag.rst.txt)


---

## 🔹 021. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addPyFile.html

# pyspark.SparkContext.addPyFile#

SparkContext.addPyFile(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addPyFile)#
    

Add a .py or .zip dependency for all tasks to be executed on this SparkContext in the future. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

New in version 0.7.0.

Parameters
    

**path** str
    

can be either a .py file or .zip dependency.

See also

[`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addPyFile.rst.txt)


---

## 🔹 022. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.applicationId.html

# pyspark.SparkContext.applicationId#

_property _SparkContext.applicationId#
    

A unique identifier for the Spark application. Its format depends on the scheduler implementation.

  * in case of local spark app something like âlocal-1433865536131â

  * in case of YARN something like âapplication_1433865536131_34483â




New in version 1.5.0.

Examples
    
    
    >>> sc.applicationId  
    'local-...'
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.applicationId.rst.txt)


---

## 🔹 023. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.binaryFiles.html

# pyspark.SparkContext.binaryFiles#

SparkContext.binaryFiles(_path_ , _minPartitions =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.binaryFiles)#
    

Read a directory of binary files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI as a byte array. Each file is read as a single record and returned in a key-value pair, where the key is the path of each file, the value is the content of each file.

New in version 1.3.0.

Parameters
    

**path** str
    

directory to the input data files, the path can be comma separated paths as a list of inputs

**minPartitions** int, optional
    

suggested minimum number of partitions for the resulting RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD representing path-content pairs from the file(s).

See also

[`SparkContext.binaryRecords()`](pyspark.SparkContext.binaryRecords.html#pyspark.SparkContext.binaryRecords "pyspark.SparkContext.binaryRecords")
    

Notes

Small files are preferred, large file is also allowable, but may cause bad performance.

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="binaryFiles") as d:
    ...     # Write a temporary binary file
    ...     with open(os.path.join(d, "1.bin"), "wb") as f1:
    ...         _ = f1.write(b"binary data I")
    ...
    ...     # Write another temporary binary file
    ...     with open(os.path.join(d, "2.bin"), "wb") as f2:
    ...         _ = f2.write(b"binary data II")
    ...
    ...     collected = sorted(sc.binaryFiles(d).collect())
    
    
    
    >>> collected
    [('.../1.bin', b'binary data I'), ('.../2.bin', b'binary data II')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.binaryFiles.rst.txt)


---

## 🔹 024. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.binaryRecords.html

# pyspark.SparkContext.binaryRecords#

SparkContext.binaryRecords(_path_ , _recordLength_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.binaryRecords)#
    

Load data from a flat binary file, assuming each record is a set of numbers with the specified numerical format (see ByteBuffer), and the number of bytes per record is constant.

New in version 1.3.0.

Parameters
    

**path** str
    

Directory to the input data files

**recordLength** int
    

The length at which to split the records

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of data with values, represented as byte arrays

See also

[`SparkContext.binaryFiles()`](pyspark.SparkContext.binaryFiles.html#pyspark.SparkContext.binaryFiles "pyspark.SparkContext.binaryFiles")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="binaryRecords") as d:
    ...     # Write a temporary file
    ...     with open(os.path.join(d, "1.bin"), "w") as f:
    ...         for i in range(3):
    ...             _ = f.write("%04d" % i)
    ...
    ...     # Write another file
    ...     with open(os.path.join(d, "2.bin"), "w") as f:
    ...         for i in [-1, -2, -10]:
    ...             _ = f.write("%04d" % i)
    ...
    ...     collected = sorted(sc.binaryRecords(d, 4).collect())
    
    
    
    >>> collected
    [b'-001', b'-002', b'-010', b'0000', b'0001', b'0002']
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.binaryRecords.rst.txt)


---

## 🔹 025. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.broadcast.html

# pyspark.SparkContext.broadcast#

SparkContext.broadcast(_value_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.broadcast)#
    

Broadcast a read-only variable to the cluster, returning a [`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object for reading it in distributed functions. The variable will be sent to each cluster only once.

New in version 0.7.0.

Parameters
    

**value** T
    

value to broadcast to the Spark nodes

Returns
    

[`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast")
    

[`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object, a read-only variable cached on each machine

Examples
    
    
    >>> mapping = {1: 10001, 2: 10002}
    >>> bc = sc.broadcast(mapping)
    
    
    
    >>> rdd = sc.range(5)
    >>> rdd2 = rdd.map(lambda i: bc.value[i] if i in bc.value else -1)
    >>> rdd2.collect()
    [-1, 10001, 10002, -1, -1]
    
    
    
    >>> bc.destroy()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.broadcast.rst.txt)


---

## 🔹 026. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelAllJobs.html

# pyspark.SparkContext.cancelAllJobs#

SparkContext.cancelAllJobs()[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelAllJobs)#
    

Cancel all jobs that have been scheduled or are running.

New in version 1.1.0.

See also

[`SparkContext.cancelJobGroup()`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.runJob()`](pyspark.SparkContext.runJob.html#pyspark.SparkContext.runJob "pyspark.SparkContext.runJob")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelAllJobs.rst.txt)


---

## 🔹 027. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelJobGroup.html

# pyspark.SparkContext.cancelJobGroup#

SparkContext.cancelJobGroup(_groupId_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelJobGroup)#
    

Cancel active jobs for the specified group. See [`SparkContext.setJobGroup()`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup"). for more information.

New in version 1.1.0.

Parameters
    

**groupId** str
    

The group ID to cancel the job.

See also

[`SparkContext.setJobGroup()`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelJobGroup.rst.txt)


---

## 🔹 028. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelJobsWithTag.html

# pyspark.SparkContext.cancelJobsWithTag#

SparkContext.cancelJobsWithTag(_tag_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelJobsWithTag)#
    

Cancel active jobs that have the specified tag. See [`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag").

New in version 3.5.0.

Parameters
    

**tag** str
    

The tag to be cancelled. Cannot contain â,â (comma) character.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelJobsWithTag.rst.txt)


---

## 🔹 029. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.clearJobTags.html

# pyspark.SparkContext.clearJobTags#

SparkContext.clearJobTags()[[source]](../../_modules/pyspark/core/context.html#SparkContext.clearJobTags)#
    

Clear the current threadâs job tags.

New in version 3.5.0.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> sc.addJobTag("job_to_cancel")
    >>> sc.clearJobTags()
    >>> sc.getJobTags()
    set()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.clearJobTags.rst.txt)


---

## 🔹 030. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.defaultMinPartitions.html

# pyspark.SparkContext.defaultMinPartitions#

_property _SparkContext.defaultMinPartitions#
    

Default min number of partitions for Hadoop RDDs when not given by user

New in version 1.1.0.

Examples
    
    
    >>> sc.defaultMinPartitions > 0
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.defaultMinPartitions.rst.txt)


---

## 🔹 031. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.defaultParallelism.html

# pyspark.SparkContext.defaultParallelism#

_property _SparkContext.defaultParallelism#
    

Default level of parallelism to use when not given by user (e.g. for reduce tasks)

New in version 0.7.0.

Examples
    
    
    >>> sc.defaultParallelism > 0
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.defaultParallelism.rst.txt)


---

## 🔹 032. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.dump_profiles.html

# pyspark.SparkContext.dump_profiles#

SparkContext.dump_profiles(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.dump_profiles)#
    

Dump the profile stats into directory path

New in version 1.2.0.

See also

[`SparkContext.show_profiles()`](pyspark.SparkContext.show_profiles.html#pyspark.SparkContext.show_profiles "pyspark.SparkContext.show_profiles")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.dump_profiles.rst.txt)


---

## 🔹 033. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.emptyRDD.html

# pyspark.SparkContext.emptyRDD#

SparkContext.emptyRDD()[[source]](../../_modules/pyspark/core/context.html#SparkContext.emptyRDD)#
    

Create an [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that has no partitions or elements.

New in version 1.5.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

An empty RDD

Examples
    
    
    >>> sc.emptyRDD()
    EmptyRDD...
    >>> sc.emptyRDD().count()
    0
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.emptyRDD.rst.txt)


---

## 🔹 034. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getCheckpointDir.html

# pyspark.SparkContext.getCheckpointDir#

SparkContext.getCheckpointDir()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getCheckpointDir)#
    

Return the directory where RDDs are checkpointed. Returns None if no checkpoint directory has been set.

New in version 3.1.0.

See also

[`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")
    
[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`RDD.getCheckpointFile()`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getCheckpointDir.rst.txt)


---

## 🔹 035. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getConf.html

# pyspark.SparkContext.getConf#

SparkContext.getConf()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getConf)#
    

Return a copy of this SparkContextâs configuration [`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf").

New in version 2.1.0.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getConf.rst.txt)


---

## 🔹 036. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getJobTags.html

# pyspark.SparkContext.getJobTags#

SparkContext.getJobTags()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getJobTags)#
    

Get the tags that are currently set to be assigned to all the jobs started by this thread.

New in version 3.5.0.

Returns
    

set of str
    

the tags that are currently set to be assigned to all the jobs started by this thread.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> sc.addJobTag("job_to_cancel")
    >>> sc.getJobTags()
    {'job_to_cancel'}
    >>> sc.clearJobTags()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getJobTags.rst.txt)


---

## 🔹 037. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getLocalProperty.html

# pyspark.SparkContext.getLocalProperty#

SparkContext.getLocalProperty(_key_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getLocalProperty)#
    

Get a local property set in this thread, or null if it is missing. See [`setLocalProperty()`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty").

New in version 1.0.0.

See also

[`SparkContext.setLocalProperty()`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getLocalProperty.rst.txt)


---

## 🔹 038. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getOrCreate.html

# pyspark.SparkContext.getOrCreate#

_classmethod _SparkContext.getOrCreate(_conf =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getOrCreate)#
    

Get or instantiate a [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") and register it as a singleton object.

New in version 1.4.0.

Parameters
    

**conf**[` SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf"), optional
    

[`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf") that will be used for initialization of the [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext").

Returns
    

[`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext")
    

current [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), or a new one if it wasnât created before the function call.

Examples
    
    
    >>> SparkContext.getOrCreate()
    <SparkContext ...>
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getOrCreate.rst.txt)


---

## 🔹 039. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getSystemProperty.html

# pyspark.SparkContext.getSystemProperty#

_classmethod _SparkContext.getSystemProperty(_key_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getSystemProperty)#
    

Get a Java system property, such as java.home.

New in version 4.0.0.

Parameters
    

**key** str
    

The key of a new Java system property.

Examples
    
    
    >>> sc.getSystemProperty("SPARK_SUBMIT")
    'true'
    >>> _ = sc.getSystemProperty("java.home")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getSystemProperty.rst.txt)


---

## 🔹 040. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.hadoopFile.html

# pyspark.SparkContext.hadoopFile#

SparkContext.hadoopFile(_path_ , _inputFormatClass_ , _keyClass_ , _valueClass_ , _keyConverter =None_, _valueConverter =None_, _conf =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.hadoopFile)#
    

Read an âoldâ Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. The mechanism is the same as for meth:SparkContext.sequenceFile.

New in version 1.1.0.

A Hadoop configuration can be passed in as a Python dict. This will be converted into a Configuration in Java.

Parameters
    

**path** str
    

path to Hadoop file

**inputFormatClass** str
    

fully qualified classname of Hadoop InputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.input.TextInputFormatâ)

**keyClass** str
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter

**valueConverter** str, optional
    

fully qualified name of a function returning value WritableConverter

**conf** dict, optional
    

Hadoop configuration, passed in as a dict

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`SparkContext.newAPIHadoopFile()`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")
    
[`SparkContext.hadoopRDD()`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="hadoopFile") as d:
    ...     path = os.path.join(d, "old_hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsHadoopFile(path, output_format_class, key_class, value_class)
    ...
    ...     loaded = sc.hadoopFile(path, input_format_class, key_class, value_class)
    ...     collected = sorted(loaded.collect())
    
    
    
    >>> collected
    [(0, '1\t'), (0, '1\ta'), (0, '3\tx')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.hadoopFile.rst.txt)


---

## 🔹 041. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html

# pyspark.SparkContext#

_class _pyspark.SparkContext(_master=None_ , _appName=None_ , _sparkHome=None_ , _pyFiles=None_ , _environment=None_ , _batchSize=0_ , _serializer=CloudPickleSerializer()_ , _conf=None_ , _gateway=None_ , _jsc=None_ , _profiler_cls= <class 'pyspark.profiler.BasicProfiler'>_, _udf_profiler_cls= <class 'pyspark.profiler.UDFBasicProfiler'>_, _memory_profiler_cls= <class 'pyspark.profiler.MemoryProfiler'>_)[[source]](../../_modules/pyspark/core/context.html#SparkContext)#
    

Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, and can be used to create [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") and broadcast variables on that cluster.

When you create a new SparkContext, at least the master and app name should be set, either through the named parameters here or through conf.

Parameters
    

**master** str, optional
    

Cluster URL to connect to (e.g. spark://host:port, local[4]).

**appName** str, optional
    

A name for your job, to display on the cluster web UI.

**sparkHome** str, optional
    

Location where Spark is installed on cluster nodes.

**pyFiles** list, optional
    

Collection of .zip or .py files to send to the cluster and add to PYTHONPATH. These can be paths on the local file system or HDFS, HTTP, HTTPS, or FTP URLs.

**environment** dict, optional
    

A dictionary of environment variables to set on worker nodes.

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. Set 1 to disable batching, 0 to automatically choose the batch size based on object sizes, or -1 to use an unlimited batch size

**serializer**` Serializer`, optional, default `CPickleSerializer`
    

The serializer for RDDs.

**conf**[` SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf"), optional
    

An object setting Spark properties.

**gateway** class:py4j.java_gateway.JavaGateway, optional
    

Use an existing gateway and JVM, otherwise a new JVM will be instantiated. This is only used internally.

**jsc** class:py4j.java_gateway.JavaObject, optional
    

The JavaSparkContext instance. This is only used internally.

**profiler_cls** type, optional, default `BasicProfiler`
    

A class of custom Profiler used to do profiling

**udf_profiler_cls** type, optional, default `UDFBasicProfiler`
    

A class of custom Profiler used to do udf profiling

Notes

Only one `SparkContext` should be active per JVM. You must stop() the active `SparkContext` before creating a new one.

`SparkContext` instance is not supported to share across multiple processes out of the box, and PySpark does not guarantee multi-processing execution. Use threads instead for concurrent processing purpose.

Examples
    
    
    >>> from pyspark.core.context import SparkContext
    >>> sc = SparkContext('local', 'test')
    >>> sc2 = SparkContext('local', 'test2') 
    Traceback (most recent call last):
        ...
    ValueError: ...
    

Methods

[`accumulator`](pyspark.SparkContext.accumulator.html#pyspark.SparkContext.accumulator "pyspark.SparkContext.accumulator")(value[,Â accum_param]) | Create an [`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator") with the given initial value, using a given [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") helper object to define how to add values of the data type if provided.  
---|---  
[`addArchive`](pyspark.SparkContext.addArchive.html#pyspark.SparkContext.addArchive "pyspark.SparkContext.addArchive")(path) | Add an archive to be downloaded with this Spark job on every node.  
[`addFile`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")(path[,Â recursive]) | Add a file to be downloaded with this Spark job on every node.  
[`addJobTag`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")(tag) | Add a tag to be assigned to all the jobs started by this thread.  
[`addPyFile`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")(path) | Add a .py or .zip dependency for all tasks to be executed on this SparkContext in the future.  
[`binaryFiles`](pyspark.SparkContext.binaryFiles.html#pyspark.SparkContext.binaryFiles "pyspark.SparkContext.binaryFiles")(path[,Â minPartitions]) | Read a directory of binary files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI as a byte array.  
[`binaryRecords`](pyspark.SparkContext.binaryRecords.html#pyspark.SparkContext.binaryRecords "pyspark.SparkContext.binaryRecords")(path,Â recordLength) | Load data from a flat binary file, assuming each record is a set of numbers with the specified numerical format (see ByteBuffer), and the number of bytes per record is constant.  
[`broadcast`](pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast")(value) | Broadcast a read-only variable to the cluster, returning a [`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object for reading it in distributed functions.  
[`cancelAllJobs`](pyspark.SparkContext.cancelAllJobs.html#pyspark.SparkContext.cancelAllJobs "pyspark.SparkContext.cancelAllJobs")() | Cancel all jobs that have been scheduled or are running.  
[`cancelJobGroup`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")(groupId) | Cancel active jobs for the specified group.  
[`cancelJobsWithTag`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")(tag) | Cancel active jobs that have the specified tag.  
[`clearJobTags`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")() | Clear the current thread's job tags.  
[`dump_profiles`](pyspark.SparkContext.dump_profiles.html#pyspark.SparkContext.dump_profiles "pyspark.SparkContext.dump_profiles")(path) | Dump the profile stats into directory path  
[`emptyRDD`](pyspark.SparkContext.emptyRDD.html#pyspark.SparkContext.emptyRDD "pyspark.SparkContext.emptyRDD")() | Create an [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that has no partitions or elements.  
[`getCheckpointDir`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")() | Return the directory where RDDs are checkpointed.  
[`getConf`](pyspark.SparkContext.getConf.html#pyspark.SparkContext.getConf "pyspark.SparkContext.getConf")() | Return a copy of this SparkContext's configuration [`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf").  
[`getJobTags`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")() | Get the tags that are currently set to be assigned to all the jobs started by this thread.  
[`getLocalProperty`](pyspark.SparkContext.getLocalProperty.html#pyspark.SparkContext.getLocalProperty "pyspark.SparkContext.getLocalProperty")(key) | Get a local property set in this thread, or null if it is missing.  
[`getOrCreate`](pyspark.SparkContext.getOrCreate.html#pyspark.SparkContext.getOrCreate "pyspark.SparkContext.getOrCreate")([conf]) | Get or instantiate a `SparkContext` and register it as a singleton object.  
[`getSystemProperty`](pyspark.SparkContext.getSystemProperty.html#pyspark.SparkContext.getSystemProperty "pyspark.SparkContext.getSystemProperty")(key) | Get a Java system property, such as java.home.  
[`hadoopFile`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")(path,Â inputFormatClass,Â keyClass,Â ...) | Read an 'old' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`hadoopRDD`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")(inputFormatClass,Â keyClass,Â valueClass) | Read an 'old' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`newAPIHadoopFile`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")(path,Â inputFormatClass,Â ...) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`newAPIHadoopRDD`](pyspark.SparkContext.newAPIHadoopRDD.html#pyspark.SparkContext.newAPIHadoopRDD "pyspark.SparkContext.newAPIHadoopRDD")(inputFormatClass,Â keyClass,Â ...) | Read a 'new API' Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict.  
[`parallelize`](pyspark.SparkContext.parallelize.html#pyspark.SparkContext.parallelize "pyspark.SparkContext.parallelize")(c[,Â numSlices]) | Distribute a local Python collection to form an RDD.  
[`pickleFile`](pyspark.SparkContext.pickleFile.html#pyspark.SparkContext.pickleFile "pyspark.SparkContext.pickleFile")(name[,Â minPartitions]) | Load an RDD previously saved using [`RDD.saveAsPickleFile()`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile") method.  
[`range`](pyspark.SparkContext.range.html#pyspark.SparkContext.range "pyspark.SparkContext.range")(start[,Â end,Â step,Â numSlices]) | Create a new RDD of int containing elements from start to end (exclusive), increased by step every element.  
[`removeJobTag`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")(tag) | Remove a tag previously added to be assigned to all the jobs started by this thread.  
[`runJob`](pyspark.SparkContext.runJob.html#pyspark.SparkContext.runJob "pyspark.SparkContext.runJob")(rdd,Â partitionFunc[,Â partitions,Â ...]) | Executes the given partitionFunc on the specified set of partitions, returning the result as an array of elements.  
[`sequenceFile`](pyspark.SparkContext.sequenceFile.html#pyspark.SparkContext.sequenceFile "pyspark.SparkContext.sequenceFile")(path[,Â keyClass,Â valueClass,Â ...]) | Read a Hadoop SequenceFile with arbitrary key and value Writable class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
[`setCheckpointDir`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")(dirName) | Set the directory under which RDDs are going to be checkpointed.  
[`setInterruptOnCancel`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")(interruptOnCancel) | Set the behavior of job cancellation from jobs started in this thread.  
[`setJobDescription`](pyspark.SparkContext.setJobDescription.html#pyspark.SparkContext.setJobDescription "pyspark.SparkContext.setJobDescription")(value) | Set a human readable description of the current job.  
[`setJobGroup`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")(groupId,Â description[,Â ...]) | Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.  
[`setLocalProperty`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty")(key,Â value) | Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.  
[`setLogLevel`](pyspark.SparkContext.setLogLevel.html#pyspark.SparkContext.setLogLevel "pyspark.SparkContext.setLogLevel")(logLevel) | Control our logLevel.  
[`setSystemProperty`](pyspark.SparkContext.setSystemProperty.html#pyspark.SparkContext.setSystemProperty "pyspark.SparkContext.setSystemProperty")(key,Â value) | Set a Java system property, such as spark.executor.memory.  
[`show_profiles`](pyspark.SparkContext.show_profiles.html#pyspark.SparkContext.show_profiles "pyspark.SparkContext.show_profiles")() | Print the profile stats to stdout  
[`sparkUser`](pyspark.SparkContext.sparkUser.html#pyspark.SparkContext.sparkUser "pyspark.SparkContext.sparkUser")() | Get SPARK_USER for user who is running SparkContext.  
[`statusTracker`](pyspark.SparkContext.statusTracker.html#pyspark.SparkContext.statusTracker "pyspark.SparkContext.statusTracker")() | Return `StatusTracker` object  
[`stop`](pyspark.SparkContext.stop.html#pyspark.SparkContext.stop "pyspark.SparkContext.stop")() | Shut down the `SparkContext`.  
[`textFile`](pyspark.SparkContext.textFile.html#pyspark.SparkContext.textFile "pyspark.SparkContext.textFile")(name[,Â minPartitions,Â use_unicode]) | Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings.  
[`union`](pyspark.SparkContext.union.html#pyspark.SparkContext.union "pyspark.SparkContext.union")(rdds) | Build the union of a list of RDDs.  
[`wholeTextFiles`](pyspark.SparkContext.wholeTextFiles.html#pyspark.SparkContext.wholeTextFiles "pyspark.SparkContext.wholeTextFiles")(path[,Â minPartitions,Â ...]) | Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.  
  
Attributes

[`PACKAGE_EXTENSIONS`](pyspark.SparkContext.PACKAGE_EXTENSIONS.html#pyspark.SparkContext.PACKAGE_EXTENSIONS "pyspark.SparkContext.PACKAGE_EXTENSIONS") |   
---|---  
[`applicationId`](pyspark.SparkContext.applicationId.html#pyspark.SparkContext.applicationId "pyspark.SparkContext.applicationId") | A unique identifier for the Spark application.  
[`defaultMinPartitions`](pyspark.SparkContext.defaultMinPartitions.html#pyspark.SparkContext.defaultMinPartitions "pyspark.SparkContext.defaultMinPartitions") | Default min number of partitions for Hadoop RDDs when not given by user  
[`defaultParallelism`](pyspark.SparkContext.defaultParallelism.html#pyspark.SparkContext.defaultParallelism "pyspark.SparkContext.defaultParallelism") | Default level of parallelism to use when not given by user (e.g.  
[`listArchives`](pyspark.SparkContext.listArchives.html#pyspark.SparkContext.listArchives "pyspark.SparkContext.listArchives") | Returns a list of archive paths that are added to resources.  
[`listFiles`](pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles") | Returns a list of file paths that are added to resources.  
[`resources`](pyspark.SparkContext.resources.html#pyspark.SparkContext.resources "pyspark.SparkContext.resources") | Return the resource information of this `SparkContext`.  
[`startTime`](pyspark.SparkContext.startTime.html#pyspark.SparkContext.startTime "pyspark.SparkContext.startTime") | Return the epoch time when the `SparkContext` was started.  
[`uiWebUrl`](pyspark.SparkContext.uiWebUrl.html#pyspark.SparkContext.uiWebUrl "pyspark.SparkContext.uiWebUrl") | Return the URL of the SparkUI instance started by this `SparkContext`  
[`version`](pyspark.SparkContext.version.html#pyspark.SparkContext.version "pyspark.SparkContext.version") | The version of Spark on which this application is running.  
`serializer` |   
`profiler_collector` |   
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.rst.txt)


---

## 🔹 042. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.html

# pyspark.RDD#

_class _pyspark.RDD(_jrdd_ , _ctx_ , _jrdd_deserializer =AutoBatchedSerializer(CloudPickleSerializer())_)[[source]](../../_modules/pyspark/core/rdd.html#RDD)#
    

A Resilient Distributed Dataset (RDD), the basic abstraction in Spark. Represents an immutable, partitioned collection of elements that can be operated on in parallel.

Methods

[`aggregate`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")(zeroValue,Â seqOp,Â combOp) | Aggregate the elements of each partition, and then the results for all the partitions, using a given combine functions and a neutral "zero value."  
---|---  
[`aggregateByKey`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")(zeroValue,Â seqFunc,Â combFunc) | Aggregate the values of each key, using given combine functions and a neutral "zero value".  
[`barrier`](pyspark.RDD.barrier.html#pyspark.RDD.barrier "pyspark.RDD.barrier")() | Marks the current stage as a barrier stage, where Spark must launch all tasks together.  
[`cache`](pyspark.RDD.cache.html#pyspark.RDD.cache "pyspark.RDD.cache")() | Persist this RDD with the default storage level (MEMORY_ONLY).  
[`cartesian`](pyspark.RDD.cartesian.html#pyspark.RDD.cartesian "pyspark.RDD.cartesian")(other) | Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements `(a, b)` where `a` is in self and `b` is in other.  
[`checkpoint`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")() | Mark this RDD for checkpointing.  
[`cleanShuffleDependencies`](pyspark.RDD.cleanShuffleDependencies.html#pyspark.RDD.cleanShuffleDependencies "pyspark.RDD.cleanShuffleDependencies")([blocking]) | Removes an RDD's shuffles and it's non-persisted ancestors.  
[`coalesce`](pyspark.RDD.coalesce.html#pyspark.RDD.coalesce "pyspark.RDD.coalesce")(numPartitions[,Â shuffle]) | Return a new RDD that is reduced into numPartitions partitions.  
[`cogroup`](pyspark.RDD.cogroup.html#pyspark.RDD.cogroup "pyspark.RDD.cogroup")(other[,Â numPartitions]) | For each key k in self or other, return a resulting RDD that contains a tuple with the list of values for that key in self as well as other.  
[`collect`](pyspark.RDD.collect.html#pyspark.RDD.collect "pyspark.RDD.collect")() | Return a list that contains all the elements in this RDD.  
[`collectAsMap`](pyspark.RDD.collectAsMap.html#pyspark.RDD.collectAsMap "pyspark.RDD.collectAsMap")() | Return the key-value pairs in this RDD to the master as a dictionary.  
[`collectWithJobGroup`](pyspark.RDD.collectWithJobGroup.html#pyspark.RDD.collectWithJobGroup "pyspark.RDD.collectWithJobGroup")(groupId,Â description[,Â ...]) | When collect rdd, use this method to specify job group.  
[`combineByKey`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")(createCombiner,Â mergeValue,Â ...) | Generic function to combine the elements for each key using a custom set of aggregation functions.  
[`count`](pyspark.RDD.count.html#pyspark.RDD.count "pyspark.RDD.count")() | Return the number of elements in this RDD.  
[`countApprox`](pyspark.RDD.countApprox.html#pyspark.RDD.countApprox "pyspark.RDD.countApprox")(timeout[,Â confidence]) | Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.  
[`countApproxDistinct`](pyspark.RDD.countApproxDistinct.html#pyspark.RDD.countApproxDistinct "pyspark.RDD.countApproxDistinct")([relativeSD]) | Return approximate number of distinct elements in the RDD.  
[`countByKey`](pyspark.RDD.countByKey.html#pyspark.RDD.countByKey "pyspark.RDD.countByKey")() | Count the number of elements for each key, and return the result to the master as a dictionary.  
[`countByValue`](pyspark.RDD.countByValue.html#pyspark.RDD.countByValue "pyspark.RDD.countByValue")() | Return the count of each unique value in this RDD as a dictionary of (value, count) pairs.  
[`distinct`](pyspark.RDD.distinct.html#pyspark.RDD.distinct "pyspark.RDD.distinct")([numPartitions]) | Return a new RDD containing the distinct elements in this RDD.  
[`filter`](pyspark.RDD.filter.html#pyspark.RDD.filter "pyspark.RDD.filter")(f) | Return a new RDD containing only the elements that satisfy a predicate.  
[`first`](pyspark.RDD.first.html#pyspark.RDD.first "pyspark.RDD.first")() | Return the first element in this RDD.  
[`flatMap`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")(f[,Â preservesPartitioning]) | Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  
[`flatMapValues`](pyspark.RDD.flatMapValues.html#pyspark.RDD.flatMapValues "pyspark.RDD.flatMapValues")(f) | Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDD's partitioning.  
[`fold`](pyspark.RDD.fold.html#pyspark.RDD.fold "pyspark.RDD.fold")(zeroValue,Â op) | Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value."  
[`foldByKey`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")(zeroValue,Â func[,Â numPartitions,Â ...]) | Merge the values for each key using an associative function "func" and a neutral "zeroValue" which may be added to the result an arbitrary number of times, and must not change the result (e.g., 0 for addition, or 1 for multiplication.).  
[`foreach`](pyspark.RDD.foreach.html#pyspark.RDD.foreach "pyspark.RDD.foreach")(f) | Applies a function to all elements of this RDD.  
[`foreachPartition`](pyspark.RDD.foreachPartition.html#pyspark.RDD.foreachPartition "pyspark.RDD.foreachPartition")(f) | Applies a function to each partition of this RDD.  
[`fullOuterJoin`](pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`getCheckpointFile`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")() | Gets the name of the file to which this RDD was checkpointed  
[`getNumPartitions`](pyspark.RDD.getNumPartitions.html#pyspark.RDD.getNumPartitions "pyspark.RDD.getNumPartitions")() | Returns the number of partitions in RDD  
[`getResourceProfile`](pyspark.RDD.getResourceProfile.html#pyspark.RDD.getResourceProfile "pyspark.RDD.getResourceProfile")() | Get the [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") specified with this RDD or None if it wasn't specified.  
[`getStorageLevel`](pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")() | Get the RDD's current storage level.  
[`glom`](pyspark.RDD.glom.html#pyspark.RDD.glom "pyspark.RDD.glom")() | Return an RDD created by coalescing all elements within each partition into a list.  
[`groupBy`](pyspark.RDD.groupBy.html#pyspark.RDD.groupBy "pyspark.RDD.groupBy")(f[,Â numPartitions,Â partitionFunc]) | Return an RDD of grouped items.  
[`groupByKey`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")([numPartitions,Â partitionFunc]) | Group the values for each key in the RDD into a single sequence.  
[`groupWith`](pyspark.RDD.groupWith.html#pyspark.RDD.groupWith "pyspark.RDD.groupWith")(other,Â *others) | Alias for cogroup but with support for multiple RDDs.  
[`histogram`](pyspark.RDD.histogram.html#pyspark.RDD.histogram "pyspark.RDD.histogram")(buckets) | Compute a histogram using the provided buckets.  
[`id`](pyspark.RDD.id.html#pyspark.RDD.id "pyspark.RDD.id")() | A unique ID for this RDD (within its SparkContext).  
[`intersection`](pyspark.RDD.intersection.html#pyspark.RDD.intersection "pyspark.RDD.intersection")(other) | Return the intersection of this RDD and another one.  
[`isCheckpointed`](pyspark.RDD.isCheckpointed.html#pyspark.RDD.isCheckpointed "pyspark.RDD.isCheckpointed")() | Return whether this RDD is checkpointed and materialized, either reliably or locally.  
[`isEmpty`](pyspark.RDD.isEmpty.html#pyspark.RDD.isEmpty "pyspark.RDD.isEmpty")() | Returns true if and only if the RDD contains no elements at all.  
[`isLocallyCheckpointed`](pyspark.RDD.isLocallyCheckpointed.html#pyspark.RDD.isLocallyCheckpointed "pyspark.RDD.isLocallyCheckpointed")() | Return whether this RDD is marked for local checkpointing.  
[`join`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")(other[,Â numPartitions]) | Return an RDD containing all pairs of elements with matching keys in self and other.  
[`keyBy`](pyspark.RDD.keyBy.html#pyspark.RDD.keyBy "pyspark.RDD.keyBy")(f) | Creates tuples of the elements in this RDD by applying f.  
[`keys`](pyspark.RDD.keys.html#pyspark.RDD.keys "pyspark.RDD.keys")() | Return an RDD with the keys of each tuple.  
[`leftOuterJoin`](pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")(other[,Â numPartitions]) | Perform a left outer join of self and other.  
[`localCheckpoint`](pyspark.RDD.localCheckpoint.html#pyspark.RDD.localCheckpoint "pyspark.RDD.localCheckpoint")() | Mark this RDD for local checkpointing using Spark's existing caching layer.  
[`lookup`](pyspark.RDD.lookup.html#pyspark.RDD.lookup "pyspark.RDD.lookup")(key) | Return the list of values in the RDD for key key.  
[`map`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each element of this RDD.  
[`mapPartitions`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")(f[,Â preservesPartitioning]) | Return a new RDD by applying a function to each partition of this RDD.  
[`mapPartitionsWithIndex`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`mapPartitionsWithSplit`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")(f[,Â ...]) | Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.  
[`mapValues`](pyspark.RDD.mapValues.html#pyspark.RDD.mapValues "pyspark.RDD.mapValues")(f) | Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD's partitioning.  
[`max`](pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")([key]) | Find the maximum item in this RDD.  
[`mean`](pyspark.RDD.mean.html#pyspark.RDD.mean "pyspark.RDD.mean")() | Compute the mean of this RDD's elements.  
[`meanApprox`](pyspark.RDD.meanApprox.html#pyspark.RDD.meanApprox "pyspark.RDD.meanApprox")(timeout[,Â confidence]) | Approximate operation to return the mean within a timeout or meet the confidence.  
[`min`](pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")([key]) | Find the minimum item in this RDD.  
[`name`](pyspark.RDD.name.html#pyspark.RDD.name "pyspark.RDD.name")() | Return the name of this RDD.  
[`partitionBy`](pyspark.RDD.partitionBy.html#pyspark.RDD.partitionBy "pyspark.RDD.partitionBy")(numPartitions[,Â partitionFunc]) | Return a copy of the RDD partitioned using the specified partitioner.  
[`persist`](pyspark.RDD.persist.html#pyspark.RDD.persist "pyspark.RDD.persist")([storageLevel]) | Set this RDD's storage level to persist its values across operations after the first time it is computed.  
[`pipe`](pyspark.RDD.pipe.html#pyspark.RDD.pipe "pyspark.RDD.pipe")(command[,Â env,Â checkCode]) | Return an RDD created by piping elements to a forked external process.  
[`randomSplit`](pyspark.RDD.randomSplit.html#pyspark.RDD.randomSplit "pyspark.RDD.randomSplit")(weights[,Â seed]) | Randomly splits this RDD with the provided weights.  
[`reduce`](pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")(f) | Reduces the elements of this RDD using the specified commutative and associative binary operator.  
[`reduceByKey`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")(func[,Â numPartitions,Â partitionFunc]) | Merge the values for each key using an associative and commutative reduce function.  
[`reduceByKeyLocally`](pyspark.RDD.reduceByKeyLocally.html#pyspark.RDD.reduceByKeyLocally "pyspark.RDD.reduceByKeyLocally")(func) | Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a dictionary.  
[`repartition`](pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")(numPartitions) | Return a new RDD that has exactly numPartitions partitions.  
[`repartitionAndSortWithinPartitions`](pyspark.RDD.repartitionAndSortWithinPartitions.html#pyspark.RDD.repartitionAndSortWithinPartitions "pyspark.RDD.repartitionAndSortWithinPartitions")([...]) | Repartition the RDD according to the given partitioner and, within each resulting partition, sort records by their keys.  
[`rightOuterJoin`](pyspark.RDD.rightOuterJoin.html#pyspark.RDD.rightOuterJoin "pyspark.RDD.rightOuterJoin")(other[,Â numPartitions]) | Perform a right outer join of self and other.  
[`sample`](pyspark.RDD.sample.html#pyspark.RDD.sample "pyspark.RDD.sample")(withReplacement,Â fraction[,Â seed]) | Return a sampled subset of this RDD.  
[`sampleByKey`](pyspark.RDD.sampleByKey.html#pyspark.RDD.sampleByKey "pyspark.RDD.sampleByKey")(withReplacement,Â fractions[,Â seed]) | Return a subset of this RDD sampled by key (via stratified sampling).  
[`sampleStdev`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")() | Compute the sample standard deviation of this RDD's elements (which corrects for bias in estimating the standard deviation by dividing by N-1 instead of N).  
[`sampleVariance`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")() | Compute the sample variance of this RDD's elements (which corrects for bias in estimating the variance by dividing by N-1 instead of N).  
[`saveAsHadoopDataset`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")(conf[,Â keyConverter,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`saveAsHadoopFile`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")(path,Â outputFormatClass[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package).  
[`saveAsNewAPIHadoopDataset`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")(conf[,Â ...]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`saveAsNewAPIHadoopFile`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")(path,Â outputFormatClass) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package).  
[`saveAsPickleFile`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile")(path[,Â batchSize]) | Save this RDD as a SequenceFile of serialized objects.  
[`saveAsSequenceFile`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")(path[,Â compressionCodecClass]) | Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the "org.apache.hadoop.io.Writable" types that we convert from the RDD's key and value types.  
[`saveAsTextFile`](pyspark.RDD.saveAsTextFile.html#pyspark.RDD.saveAsTextFile "pyspark.RDD.saveAsTextFile")(path[,Â compressionCodecClass]) | Save this RDD as a text file, using string representations of elements.  
[`setName`](pyspark.RDD.setName.html#pyspark.RDD.setName "pyspark.RDD.setName")(name) | Assign a name to this RDD.  
[`sortBy`](pyspark.RDD.sortBy.html#pyspark.RDD.sortBy "pyspark.RDD.sortBy")(keyfunc[,Â ascending,Â numPartitions]) | Sorts this RDD by the given keyfunc  
[`sortByKey`](pyspark.RDD.sortByKey.html#pyspark.RDD.sortByKey "pyspark.RDD.sortByKey")([ascending,Â numPartitions,Â keyfunc]) | Sorts this RDD, which is assumed to consist of (key, value) pairs.  
[`stats`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")() | Return a `StatCounter` object that captures the mean, variance and count of the RDD's elements in one operation.  
[`stdev`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")() | Compute the standard deviation of this RDD's elements.  
[`subtract`](pyspark.RDD.subtract.html#pyspark.RDD.subtract "pyspark.RDD.subtract")(other[,Â numPartitions]) | Return each value in self that is not contained in other.  
[`subtractByKey`](pyspark.RDD.subtractByKey.html#pyspark.RDD.subtractByKey "pyspark.RDD.subtractByKey")(other[,Â numPartitions]) | Return each (key, value) pair in self that has no pair with matching key in other.  
[`sum`](pyspark.RDD.sum.html#pyspark.RDD.sum "pyspark.RDD.sum")() | Add up the elements in this RDD.  
[`sumApprox`](pyspark.RDD.sumApprox.html#pyspark.RDD.sumApprox "pyspark.RDD.sumApprox")(timeout[,Â confidence]) | Approximate operation to return the sum within a timeout or meet the confidence.  
[`take`](pyspark.RDD.take.html#pyspark.RDD.take "pyspark.RDD.take")(num) | Take the first num elements of the RDD.  
[`takeOrdered`](pyspark.RDD.takeOrdered.html#pyspark.RDD.takeOrdered "pyspark.RDD.takeOrdered")(num[,Â key]) | Get the N elements from an RDD ordered in ascending order or as specified by the optional key function.  
[`takeSample`](pyspark.RDD.takeSample.html#pyspark.RDD.takeSample "pyspark.RDD.takeSample")(withReplacement,Â num[,Â seed]) | Return a fixed-size sampled subset of this RDD.  
`toDF`([schema,Â sampleRatio]) |   
[`toDebugString`](pyspark.RDD.toDebugString.html#pyspark.RDD.toDebugString "pyspark.RDD.toDebugString")() | A description of this RDD and its recursive dependencies for debugging.  
[`toLocalIterator`](pyspark.RDD.toLocalIterator.html#pyspark.RDD.toLocalIterator "pyspark.RDD.toLocalIterator")([prefetchPartitions]) | Return an iterator that contains all of the elements in this RDD.  
[`top`](pyspark.RDD.top.html#pyspark.RDD.top "pyspark.RDD.top")(num[,Â key]) | Get the top N elements from an RDD.  
[`treeAggregate`](pyspark.RDD.treeAggregate.html#pyspark.RDD.treeAggregate "pyspark.RDD.treeAggregate")(zeroValue,Â seqOp,Â combOp[,Â depth]) | Aggregates the elements of this RDD in a multi-level tree pattern.  
[`treeReduce`](pyspark.RDD.treeReduce.html#pyspark.RDD.treeReduce "pyspark.RDD.treeReduce")(f[,Â depth]) | Reduces the elements of this RDD in a multi-level tree pattern.  
[`union`](pyspark.RDD.union.html#pyspark.RDD.union "pyspark.RDD.union")(other) | Return the union of this RDD and another one.  
[`unpersist`](pyspark.RDD.unpersist.html#pyspark.RDD.unpersist "pyspark.RDD.unpersist")([blocking]) | Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  
[`values`](pyspark.RDD.values.html#pyspark.RDD.values "pyspark.RDD.values")() | Return an RDD with the values of each tuple.  
[`variance`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")() | Compute the variance of this RDD's elements.  
[`withResources`](pyspark.RDD.withResources.html#pyspark.RDD.withResources "pyspark.RDD.withResources")(profile) | Specify a [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") to use when calculating this RDD.  
[`zip`](pyspark.RDD.zip.html#pyspark.RDD.zip "pyspark.RDD.zip")(other) | Zips this RDD with another one, returning key-value pairs with the first element in each RDD second element in each RDD, etc.  
[`zipWithIndex`](pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex")() | Zips this RDD with its element indices.  
[`zipWithUniqueId`](pyspark.RDD.zipWithUniqueId.html#pyspark.RDD.zipWithUniqueId "pyspark.RDD.zipWithUniqueId")() | Zips this RDD with generated unique Long ids.  
  
Attributes

[`context`](pyspark.RDD.context.html#pyspark.RDD.context "pyspark.RDD.context") | The [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") that this RDD was created on.  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.RDD.rst.txt)


---

## 🔹 043. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.html

# pyspark.Broadcast#

_class _pyspark.Broadcast(_sc =None_, _value =None_, _pickle_registry =None_, _path =None_, _sock_file =None_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast)#
    

A broadcast variable created with [`SparkContext.broadcast()`](pyspark.SparkContext.broadcast.html#pyspark.SparkContext.broadcast "pyspark.SparkContext.broadcast"). Access its value through [`value`](pyspark.Broadcast.value.html#pyspark.Broadcast.value "pyspark.Broadcast.value").

Examples
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    >>> b.value
    [1, 2, 3, 4, 5]
    >>> spark.sparkContext.parallelize([0, 0]).flatMap(lambda x: b.value).collect()
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    >>> b.unpersist()
    
    
    
    >>> large_broadcast = spark.sparkContext.broadcast(range(10000))
    

Methods

[`destroy`](pyspark.Broadcast.destroy.html#pyspark.Broadcast.destroy "pyspark.Broadcast.destroy")([blocking]) | Destroy all data and metadata related to this broadcast variable.  
---|---  
[`dump`](pyspark.Broadcast.dump.html#pyspark.Broadcast.dump "pyspark.Broadcast.dump")(value,Â f) | Write a pickled representation of value to the open file or socket.  
[`load`](pyspark.Broadcast.load.html#pyspark.Broadcast.load "pyspark.Broadcast.load")(file) | Read a pickled representation of value from the open file or socket.  
[`load_from_path`](pyspark.Broadcast.load_from_path.html#pyspark.Broadcast.load_from_path "pyspark.Broadcast.load_from_path")(path) | Read the pickled representation of an object from the open file and return the reconstituted object hierarchy specified therein.  
[`unpersist`](pyspark.Broadcast.unpersist.html#pyspark.Broadcast.unpersist "pyspark.Broadcast.unpersist")([blocking]) | Delete cached copies of this broadcast on the executors.  
  
Attributes

[`value`](pyspark.Broadcast.value.html#pyspark.Broadcast.value "pyspark.Broadcast.value") | Return the broadcasted value  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.rst.txt)


---

## 🔹 044. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Accumulator.html

# pyspark.Accumulator#

_class _pyspark.Accumulator(_aid_ , _value_ , _accum_param_)[[source]](../../_modules/pyspark/accumulators.html#Accumulator)#
    

A shared variable that can be accumulated, i.e., has a commutative and associative âaddâ operation. Worker tasks on a Spark cluster can add values to an Accumulator with the += operator, but only the driver program is allowed to access its value, using value. Updates from the workers get propagated automatically to the driver program.

While [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") supports accumulators for primitive data types like `int` and `float`, users can also define accumulators for custom types by providing a custom [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") object. Refer to its doctest for an example.

Examples
    
    
    >>> a = sc.accumulator(1)
    >>> a.value
    1
    >>> a.value = 2
    >>> a.value
    2
    >>> a += 5
    >>> a.value
    7
    >>> sc.accumulator(1.0).value
    1.0
    >>> sc.accumulator(1j).value
    1j
    >>> rdd = sc.parallelize([1,2,3])
    >>> def f(x):
    ...     global a
    ...     a += x
    ...
    >>> rdd.foreach(f)
    >>> a.value
    13
    >>> b = sc.accumulator(0)
    >>> def g(x):
    ...     b.add(x)
    ...
    >>> rdd.foreach(g)
    >>> b.value
    6
    
    
    
    >>> rdd.map(lambda x: a.value).collect() 
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...
    
    
    
    >>> def h(x):
    ...     global a
    ...     a.value = 7
    ...
    >>> rdd.foreach(h) 
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...
    
    
    
    >>> sc.accumulator([1.0, 2.0, 3.0]) 
    Traceback (most recent call last):
        ...
    TypeError: ...
    

Methods

[`add`](pyspark.Accumulator.add.html#pyspark.Accumulator.add "pyspark.Accumulator.add")(term) | Adds a term to this accumulator's value  
---|---  
  
Attributes

[`value`](pyspark.Accumulator.value.html#pyspark.Accumulator.value "pyspark.Accumulator.value") | Get the accumulator's value; only usable in driver program  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.Accumulator.rst.txt)


---

## 🔹 045. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.AccumulatorParam.html

# pyspark.AccumulatorParam#

_class _pyspark.AccumulatorParam[[source]](../../_modules/pyspark/accumulators.html#AccumulatorParam)#
    

Helper object that defines how to accumulate values of a given type.

Examples
    
    
    >>> from pyspark.accumulators import AccumulatorParam
    >>> class VectorAccumulatorParam(AccumulatorParam):
    ...     def zero(self, value):
    ...         return [0.0] * len(value)
    ...     def addInPlace(self, val1, val2):
    ...         for i in range(len(val1)):
    ...              val1[i] += val2[i]
    ...         return val1
    >>> va = sc.accumulator([1.0, 2.0, 3.0], VectorAccumulatorParam())
    >>> va.value
    [1.0, 2.0, 3.0]
    >>> def g(x):
    ...     global va
    ...     va += [x] * 3
    ...
    >>> rdd = sc.parallelize([1,2,3])
    >>> rdd.foreach(g)
    >>> va.value
    [7.0, 8.0, 9.0]
    

Methods

[`addInPlace`](pyspark.AccumulatorParam.addInPlace.html#pyspark.AccumulatorParam.addInPlace "pyspark.AccumulatorParam.addInPlace")(value1,Â value2) | Add two values of the accumulator's data type, returning a new value; for efficiency, can also update value1 in place and return it.  
---|---  
[`zero`](pyspark.AccumulatorParam.zero.html#pyspark.AccumulatorParam.zero "pyspark.AccumulatorParam.zero")(value) | Provide a "zero value" for the type, compatible in dimensions with the provided value (e.g., a zero vector)  
  
[ __Show Source](../../_sources/reference/api/pyspark.AccumulatorParam.rst.txt)


---

## 🔹 046. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html

# pyspark.SparkConf#

_class _pyspark.SparkConf(_loadDefaults =True_, __jvm =None_, __jconf =None_)[[source]](../../_modules/pyspark/conf.html#SparkConf)#
    

Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.

Most of the time, you would create a SparkConf object with `SparkConf()`, which will load values from spark.* Java system properties as well. In this case, any parameters you set directly on the `SparkConf` object take priority over system properties.

For unit tests, you can also call `SparkConf(false)` to skip loading external settings and get the same configuration no matter what the system properties are.

All setter methods in this class support chaining. For example, you can write `conf.setMaster("local").setAppName("My app")`.

Parameters
    

**loadDefaults** bool
    

whether to load values from Java system properties (True by default)

**_jvm** class:py4j.java_gateway.JVMView
    

internal parameter used to pass a handle to the Java VM; does not need to be set by users

**_jconf** class:py4j.java_gateway.JavaObject
    

Optionally pass in an existing SparkConf handle to use its parameters

Notes

Once a SparkConf object is passed to Spark, it is cloned and can no longer be modified by the user.

Examples
    
    
    >>> from pyspark import SparkConf, SparkContext
    >>> conf = SparkConf()
    >>> conf.setMaster("local").setAppName("My app")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.master")
    'local'
    >>> conf.get("spark.app.name")
    'My app'
    >>> sc = SparkContext(conf=conf)
    >>> sc.master
    'local'
    >>> sc.appName
    'My app'
    >>> sc.sparkHome is None
    True
    
    
    
    >>> conf = SparkConf(loadDefaults=False)
    >>> conf.setSparkHome("/path")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.home")
    '/path'
    >>> conf.setExecutorEnv("VAR1", "value1")
    <pyspark.conf.SparkConf object at ...>
    >>> conf.setExecutorEnv(pairs = [("VAR3", "value3"), ("VAR4", "value4")])
    <pyspark.conf.SparkConf object at ...>
    >>> conf.get("spark.executorEnv.VAR1")
    'value1'
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.home=/path
    >>> for p in sorted(conf.getAll(), key=lambda p: p[0]):
    ...     print(p)
    ('spark.executorEnv.VAR1', 'value1')
    ('spark.executorEnv.VAR3', 'value3')
    ('spark.executorEnv.VAR4', 'value4')
    ('spark.home', '/path')
    >>> conf._jconf.setExecutorEnv("VAR5", "value5")
    JavaObject id...
    >>> print(conf.toDebugString())
    spark.executorEnv.VAR1=value1
    spark.executorEnv.VAR3=value3
    spark.executorEnv.VAR4=value4
    spark.executorEnv.VAR5=value5
    spark.home=/path
    

Methods

[`contains`](pyspark.SparkConf.contains.html#pyspark.SparkConf.contains "pyspark.SparkConf.contains")(key) | Does this configuration contain a given key?  
---|---  
[`get`](pyspark.SparkConf.get.html#pyspark.SparkConf.get "pyspark.SparkConf.get")(key[,Â defaultValue]) | Get the configured value for some key, or return a default otherwise.  
[`getAll`](pyspark.SparkConf.getAll.html#pyspark.SparkConf.getAll "pyspark.SparkConf.getAll")() | Get all values as a list of key-value pairs.  
[`set`](pyspark.SparkConf.set.html#pyspark.SparkConf.set "pyspark.SparkConf.set")(key,Â value) | Set a configuration property.  
[`setAll`](pyspark.SparkConf.setAll.html#pyspark.SparkConf.setAll "pyspark.SparkConf.setAll")(pairs) | Set multiple parameters, passed as a list of key-value pairs.  
[`setAppName`](pyspark.SparkConf.setAppName.html#pyspark.SparkConf.setAppName "pyspark.SparkConf.setAppName")(value) | Set application name.  
[`setExecutorEnv`](pyspark.SparkConf.setExecutorEnv.html#pyspark.SparkConf.setExecutorEnv "pyspark.SparkConf.setExecutorEnv")([key,Â value,Â pairs]) | Set an environment variable to be passed to executors.  
[`setIfMissing`](pyspark.SparkConf.setIfMissing.html#pyspark.SparkConf.setIfMissing "pyspark.SparkConf.setIfMissing")(key,Â value) | Set a configuration property, if not already set.  
[`setMaster`](pyspark.SparkConf.setMaster.html#pyspark.SparkConf.setMaster "pyspark.SparkConf.setMaster")(value) | Set master URL to connect to.  
[`setSparkHome`](pyspark.SparkConf.setSparkHome.html#pyspark.SparkConf.setSparkHome "pyspark.SparkConf.setSparkHome")(value) | Set path where Spark is installed on worker nodes.  
[`toDebugString`](pyspark.SparkConf.toDebugString.html#pyspark.SparkConf.toDebugString "pyspark.SparkConf.toDebugString")() | Returns a printable version of the configuration, as a list of key=value pairs, one per line.  
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.rst.txt)


---

## 🔹 047. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkFiles.html

# pyspark.SparkFiles#

_class _pyspark.SparkFiles[[source]](../../_modules/pyspark/core/files.html#SparkFiles)#
    

Resolves paths to files added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile").

SparkFiles contains only classmethods; users should not create SparkFiles instances.

Methods

[`get`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")(filename) | Get the absolute path of a file added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
---|---  
[`getRootDirectory`](pyspark.SparkFiles.getRootDirectory.html#pyspark.SparkFiles.getRootDirectory "pyspark.SparkFiles.getRootDirectory")() | Get the root directory that contains files added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").  
  
[ __Show Source](../../_sources/reference/api/pyspark.SparkFiles.rst.txt)


---

## 🔹 048. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.html

# pyspark.StorageLevel#

_class _pyspark.StorageLevel(_useDisk_ , _useMemory_ , _useOffHeap_ , _deserialized_ , _replication =1_)[[source]](../../_modules/pyspark/storagelevel.html#StorageLevel)#
    

Flags for controlling the storage of an RDD. Each StorageLevel records whether to use memory, whether to drop the RDD to disk if it falls out of memory, whether to keep the data in memory in a JAVA-specific serialized format, and whether to replicate the RDD partitions on multiple nodes. Also contains static constants for some commonly used storage levels, MEMORY_ONLY. Since the data is always serialized on the Python side, all the constants use the serialized formats.

Attributes

[`DISK_ONLY`](pyspark.StorageLevel.DISK_ONLY.html#pyspark.StorageLevel.DISK_ONLY "pyspark.StorageLevel.DISK_ONLY") |   
---|---  
[`DISK_ONLY_2`](pyspark.StorageLevel.DISK_ONLY_2.html#pyspark.StorageLevel.DISK_ONLY_2 "pyspark.StorageLevel.DISK_ONLY_2") |   
[`DISK_ONLY_3`](pyspark.StorageLevel.DISK_ONLY_3.html#pyspark.StorageLevel.DISK_ONLY_3 "pyspark.StorageLevel.DISK_ONLY_3") |   
[`MEMORY_AND_DISK`](pyspark.StorageLevel.MEMORY_AND_DISK.html#pyspark.StorageLevel.MEMORY_AND_DISK "pyspark.StorageLevel.MEMORY_AND_DISK") |   
[`MEMORY_AND_DISK_2`](pyspark.StorageLevel.MEMORY_AND_DISK_2.html#pyspark.StorageLevel.MEMORY_AND_DISK_2 "pyspark.StorageLevel.MEMORY_AND_DISK_2") |   
[`MEMORY_AND_DISK_DESER`](pyspark.StorageLevel.MEMORY_AND_DISK_DESER.html#pyspark.StorageLevel.MEMORY_AND_DISK_DESER "pyspark.StorageLevel.MEMORY_AND_DISK_DESER") |   
[`MEMORY_ONLY`](pyspark.StorageLevel.MEMORY_ONLY.html#pyspark.StorageLevel.MEMORY_ONLY "pyspark.StorageLevel.MEMORY_ONLY") |   
[`MEMORY_ONLY_2`](pyspark.StorageLevel.MEMORY_ONLY_2.html#pyspark.StorageLevel.MEMORY_ONLY_2 "pyspark.StorageLevel.MEMORY_ONLY_2") |   
`NONE` |   
[`OFF_HEAP`](pyspark.StorageLevel.OFF_HEAP.html#pyspark.StorageLevel.OFF_HEAP "pyspark.StorageLevel.OFF_HEAP") |   
  
[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.rst.txt)


---

## 🔹 049. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.html

# pyspark.TaskContext#

_class _pyspark.TaskContext[[source]](../../_modules/pyspark/taskcontext.html#TaskContext)#
    

Contextual information about a task which can be read or mutated during execution. To access the TaskContext for a running task, use: [`TaskContext.get()`](pyspark.TaskContext.get.html#pyspark.TaskContext.get "pyspark.TaskContext.get").

New in version 2.2.0.

Examples
    
    
    >>> from pyspark import TaskContext
    

Get a task context instance from [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD").
    
    
    >>> spark.sparkContext.setLocalProperty("key1", "value")
    >>> taskcontext = spark.sparkContext.parallelize([1]).map(lambda _: TaskContext.get()).first()
    >>> isinstance(taskcontext.attemptNumber(), int)
    True
    >>> isinstance(taskcontext.partitionId(), int)
    True
    >>> isinstance(taskcontext.stageId(), int)
    True
    >>> isinstance(taskcontext.taskAttemptId(), int)
    True
    >>> taskcontext.getLocalProperty("key1")
    'value'
    >>> isinstance(taskcontext.cpus(), int)
    True
    

Get a task context instance from a dataframe via Python UDF.
    
    
    >>> from pyspark.sql import Row
    >>> from pyspark.sql.functions import udf
    >>> @udf("STRUCT<anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row():
    ...    taskcontext = TaskContext.get()
    ...    return Row(
    ...        anum=taskcontext.attemptNumber(),
    ...        partid=taskcontext.partitionId(),
    ...        stageid=taskcontext.stageId(),
    ...        taskaid=taskcontext.taskAttemptId(),
    ...        prop=taskcontext.getLocalProperty("key2"),
    ...        cpus=taskcontext.cpus())
    ...
    >>> spark.sparkContext.setLocalProperty("key2", "value")
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row()).first()
    ... )
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    'value'
    >>> isinstance(cpus, int)
    True
    

Get a task context instance from a dataframe via Pandas UDF.
    
    
    >>> import pandas as pd  
    >>> from pyspark.sql.functions import pandas_udf
    >>> @pandas_udf("STRUCT<"
    ...     "anum: INT, partid: INT, stageid: INT, taskaid: INT, prop: STRING, cpus: INT>")
    ... def taskcontext_as_row(_):
    ...    taskcontext = TaskContext.get()
    ...    return pd.DataFrame({
    ...        "anum": [taskcontext.attemptNumber()],
    ...        "partid": [taskcontext.partitionId()],
    ...        "stageid": [taskcontext.stageId()],
    ...        "taskaid": [taskcontext.taskAttemptId()],
    ...        "prop": [taskcontext.getLocalProperty("key3")],
    ...        "cpus": [taskcontext.cpus()]
    ...    })  
    ...
    >>> spark.sparkContext.setLocalProperty("key3", "value")  
    >>> [(anum, partid, stageid, taskaid, prop, cpus)] = (
    ...     spark.range(1).select(taskcontext_as_row("id")).first()
    ... )  
    >>> isinstance(anum, int)
    True
    >>> isinstance(partid, int)
    True
    >>> isinstance(stageid, int)
    True
    >>> isinstance(taskaid, int)
    True
    >>> prop
    'value'
    >>> isinstance(cpus, int)
    True
    

Methods

[`attemptNumber`](pyspark.TaskContext.attemptNumber.html#pyspark.TaskContext.attemptNumber "pyspark.TaskContext.attemptNumber")() | How many times this task has been attempted.  
---|---  
[`cpus`](pyspark.TaskContext.cpus.html#pyspark.TaskContext.cpus "pyspark.TaskContext.cpus")() | CPUs allocated to the task.  
[`get`](pyspark.TaskContext.get.html#pyspark.TaskContext.get "pyspark.TaskContext.get")() | Return the currently active `TaskContext`.  
[`getLocalProperty`](pyspark.TaskContext.getLocalProperty.html#pyspark.TaskContext.getLocalProperty "pyspark.TaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`partitionId`](pyspark.TaskContext.partitionId.html#pyspark.TaskContext.partitionId "pyspark.TaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`resources`](pyspark.TaskContext.resources.html#pyspark.TaskContext.resources "pyspark.TaskContext.resources")() | Resources allocated to the task.  
[`stageId`](pyspark.TaskContext.stageId.html#pyspark.TaskContext.stageId "pyspark.TaskContext.stageId")() | The ID of the stage that this task belong to.  
[`taskAttemptId`](pyspark.TaskContext.taskAttemptId.html#pyspark.TaskContext.taskAttemptId "pyspark.TaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
  
[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.rst.txt)


---

## 🔹 050. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDDBarrier.html

# pyspark.RDDBarrier#

_class _pyspark.RDDBarrier(_rdd_)[[source]](../../_modules/pyspark/core/rdd.html#RDDBarrier)#
    

Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together. `RDDBarrier` instances are created by [`RDD.barrier()`](pyspark.RDD.barrier.html#pyspark.RDD.barrier "pyspark.RDD.barrier").

New in version 2.4.0.

Notes

This API is experimental

Methods

[`mapPartitions`](pyspark.RDDBarrier.mapPartitions.html#pyspark.RDDBarrier.mapPartitions "pyspark.RDDBarrier.mapPartitions")(f[,Â preservesPartitioning]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, where tasks are launched together in a barrier stage.  
---|---  
[`mapPartitionsWithIndex`](pyspark.RDDBarrier.mapPartitionsWithIndex.html#pyspark.RDDBarrier.mapPartitionsWithIndex "pyspark.RDDBarrier.mapPartitionsWithIndex")(f[,Â ...]) | Returns a new RDD by applying a function to each partition of the wrapped RDD, while tracking the index of the original partition.  
  
[ __Show Source](../../_sources/reference/api/pyspark.RDDBarrier.rst.txt)


---

## 🔹 051. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.html

# pyspark.BarrierTaskContext#

_class _pyspark.BarrierTaskContext[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext)#
    

A [`TaskContext`](pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage. Use [`BarrierTaskContext.get()`](pyspark.BarrierTaskContext.get.html#pyspark.BarrierTaskContext.get "pyspark.BarrierTaskContext.get") to obtain the barrier context for a running barrier task.

New in version 2.4.0.

Notes

This API is experimental

Examples

Set a barrier, and execute it with RDD.
    
    
    >>> from pyspark import BarrierTaskContext
    >>> def block_and_do_something(itr):
    ...     taskcontext = BarrierTaskContext.get()
    ...     # Do something.
    ...
    ...     # Wait until all tasks finished.
    ...     taskcontext.barrier()
    ...
    ...     return itr
    ...
    >>> rdd = spark.sparkContext.parallelize([1])
    >>> rdd.barrier().mapPartitions(block_and_do_something).collect()
    [1]
    

Methods

[`allGather`](pyspark.BarrierTaskContext.allGather.html#pyspark.BarrierTaskContext.allGather "pyspark.BarrierTaskContext.allGather")([message]) | This function blocks until all tasks in the same stage have reached this routine.  
---|---  
[`attemptNumber`](pyspark.BarrierTaskContext.attemptNumber.html#pyspark.BarrierTaskContext.attemptNumber "pyspark.BarrierTaskContext.attemptNumber")() | How many times this task has been attempted.  
[`barrier`](pyspark.BarrierTaskContext.barrier.html#pyspark.BarrierTaskContext.barrier "pyspark.BarrierTaskContext.barrier")() | Sets a global barrier and waits until all tasks in this stage hit this barrier.  
[`cpus`](pyspark.BarrierTaskContext.cpus.html#pyspark.BarrierTaskContext.cpus "pyspark.BarrierTaskContext.cpus")() | CPUs allocated to the task.  
[`get`](pyspark.BarrierTaskContext.get.html#pyspark.BarrierTaskContext.get "pyspark.BarrierTaskContext.get")() | Return the currently active `BarrierTaskContext`.  
[`getLocalProperty`](pyspark.BarrierTaskContext.getLocalProperty.html#pyspark.BarrierTaskContext.getLocalProperty "pyspark.BarrierTaskContext.getLocalProperty")(key) | Get a local property set upstream in the driver, or None if it is missing.  
[`getTaskInfos`](pyspark.BarrierTaskContext.getTaskInfos.html#pyspark.BarrierTaskContext.getTaskInfos "pyspark.BarrierTaskContext.getTaskInfos")() | Returns [`BarrierTaskInfo`](pyspark.BarrierTaskInfo.html#pyspark.BarrierTaskInfo "pyspark.BarrierTaskInfo") for all tasks in this barrier stage, ordered by partition ID.  
[`partitionId`](pyspark.BarrierTaskContext.partitionId.html#pyspark.BarrierTaskContext.partitionId "pyspark.BarrierTaskContext.partitionId")() | The ID of the RDD partition that is computed by this task.  
[`resources`](pyspark.BarrierTaskContext.resources.html#pyspark.BarrierTaskContext.resources "pyspark.BarrierTaskContext.resources")() | Resources allocated to the task.  
[`stageId`](pyspark.BarrierTaskContext.stageId.html#pyspark.BarrierTaskContext.stageId "pyspark.BarrierTaskContext.stageId")() | The ID of the stage that this task belong to.  
[`taskAttemptId`](pyspark.BarrierTaskContext.taskAttemptId.html#pyspark.BarrierTaskContext.taskAttemptId "pyspark.BarrierTaskContext.taskAttemptId")() | An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID).  
  
[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.rst.txt)


---

## 🔹 052. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskInfo.html

# pyspark.BarrierTaskInfo#

_class _pyspark.BarrierTaskInfo(_address_)[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskInfo)#
    

Carries all task infos of a barrier task.

New in version 2.4.0.

Notes

This API is experimental

Attributes
    

**address** str
    

The IPv4 address (host:port) of the executor that the barrier task is running on

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskInfo.rst.txt)


---

## 🔹 053. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.InheritableThread.html

# pyspark.InheritableThread#

_class _pyspark.InheritableThread(_target_ , _* args_, _session =None_, _** kwargs_)[[source]](../../_modules/pyspark/util.html#InheritableThread)#
    

Thread that is recommended to be used in PySpark when the pinned thread mode is enabled. The wrapper function, before calling original thread target, it inherits the inheritable properties specific to JVM thread such as `InheritableThreadLocal`, or thread local such as tags with Spark Connect.

When the pinned thread mode is off, this works as `threading.Thread`.

New in version 3.1.0.

Changed in version 3.5.0: Supports Spark Connect.

Notes

This API is experimental.

Methods

`getName`() |   
---|---  
`isDaemon`() |   
`is_alive`() | Return whether the thread is alive.  
`join`([timeout]) | Wait until the thread terminates.  
`run`() | Method representing the thread's activity.  
`setDaemon`(daemonic) |   
`setName`(name) |   
`start`() | Start the thread's activity.  
  
Attributes

`daemon` | A boolean value indicating whether this thread is a daemon thread.  
---|---  
`ident` | Thread identifier of this thread or None if it has not been started.  
`name` | A string used for identification purposes only.  
`native_id` | Native integral thread ID of this thread, or None if it has not been started.  
  
[ __Show Source](../../_sources/reference/api/pyspark.InheritableThread.rst.txt)


---

## 🔹 054. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.util.VersionUtils.html

# pyspark.util.VersionUtils#

_class _pyspark.util.VersionUtils[[source]](../../_modules/pyspark/util.html#VersionUtils)#
    

Provides utility method to determine Spark versions with given input string.

Methods

[`majorMinorVersion`](pyspark.util.VersionUtils.majorMinorVersion.html#pyspark.util.VersionUtils.majorMinorVersion "pyspark.util.VersionUtils.majorMinorVersion")(sparkVersion) | Given a Spark version string, return the (major version number, minor version number).  
---|---  
  
[ __Show Source](../../_sources/reference/api/pyspark.util.VersionUtils.rst.txt)


---

## 🔹 055. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.PACKAGE_EXTENSIONS.html

# pyspark.SparkContext.PACKAGE_EXTENSIONS#

SparkContext.PACKAGE_EXTENSIONS _ = ('.zip', '.egg', '.jar')_#
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.PACKAGE_EXTENSIONS.rst.txt)


---

## 🔹 056. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.accumulator.html

# pyspark.SparkContext.accumulator#

SparkContext.accumulator(_value_ , _accum_param =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.accumulator)#
    

Create an [`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator") with the given initial value, using a given [`AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam") helper object to define how to add values of the data type if provided. Default AccumulatorParams are used for integers and floating-point numbers if you do not provide one. For other types, a custom AccumulatorParam can be used.

New in version 0.7.0.

Parameters
    

**value** T
    

initialized value

**accum_param**[` pyspark.AccumulatorParam`](pyspark.AccumulatorParam.html#pyspark.AccumulatorParam "pyspark.AccumulatorParam"), optional
    

helper object to define how to add values

Returns
    

[`Accumulator`](pyspark.Accumulator.html#pyspark.Accumulator "pyspark.Accumulator")
    

Accumulator object, a shared variable that can be accumulated

Examples
    
    
    >>> acc = sc.accumulator(9)
    >>> acc.value
    9
    >>> acc += 1
    >>> acc.value
    10
    

Accumulator object can be accumulated in RDD operations:
    
    
    >>> rdd = sc.range(5)
    >>> def f(x):
    ...     global acc
    ...     acc += 1
    ...
    >>> rdd.foreach(f)
    >>> acc.value
    15
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.accumulator.rst.txt)


---

## 🔹 057. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addArchive.html

# pyspark.SparkContext.addArchive#

SparkContext.addArchive(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addArchive)#
    

Add an archive to be downloaded with this Spark job on every node. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") with the filename to find its download/unpacked location. The given path should be one of .zip, .tar, .tar.gz, .tgz and .jar.

New in version 3.3.0.

Parameters
    

**path** str
    

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") to find its download location.

See also

[`SparkContext.listArchives()`](pyspark.SparkContext.listArchives.html#pyspark.SparkContext.listArchives "pyspark.SparkContext.listArchives")
    
[`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored. This API is experimental.

Examples

Creates a zipped file that contains a text file written â100â.
    
    
    >>> import os
    >>> import tempfile
    >>> import zipfile
    >>> from pyspark import SparkFiles
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="addArchive") as d:
    ...     path = os.path.join(d, "test.txt")
    ...     with open(path, "w") as f:
    ...         _ = f.write("100")
    ...
    ...     zip_path1 = os.path.join(d, "test1.zip")
    ...     with zipfile.ZipFile(zip_path1, "w", zipfile.ZIP_DEFLATED) as z:
    ...         z.write(path, os.path.basename(path))
    ...
    ...     zip_path2 = os.path.join(d, "test2.zip")
    ...     with zipfile.ZipFile(zip_path2, "w", zipfile.ZIP_DEFLATED) as z:
    ...         z.write(path, os.path.basename(path))
    ...
    ...     sc.addArchive(zip_path1)
    ...     arch_list1 = sorted(sc.listArchives)
    ...
    ...     sc.addArchive(zip_path2)
    ...     arch_list2 = sorted(sc.listArchives)
    ...
    ...     # add zip_path2 twice, this addition will be ignored
    ...     sc.addArchive(zip_path2)
    ...     arch_list3 = sorted(sc.listArchives)
    ...
    ...     def func(iterator):
    ...         with open("%s/test.txt" % SparkFiles.get("test1.zip")) as f:
    ...             mul = int(f.readline())
    ...             return [x * mul for x in iterator]
    ...
    ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()
    
    
    
    >>> arch_list1
    ['file:/.../test1.zip']
    >>> arch_list2
    ['file:/.../test1.zip', 'file:/.../test2.zip']
    >>> arch_list3
    ['file:/.../test1.zip', 'file:/.../test2.zip']
    >>> collected
    [100, 200, 300, 400]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addArchive.rst.txt)


---

## 🔹 058. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addFile.html

# pyspark.SparkContext.addFile#

SparkContext.addFile(_path_ , _recursive =False_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addFile)#
    

Add a file to be downloaded with this Spark job on every node. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") with the filename to find its download location.

A directory can be given if the recursive option is set to True. Currently directories are only supported for Hadoop-supported filesystems.

New in version 0.7.0.

Parameters
    

**path** str
    

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use [`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get") to find its download location.

**recursive** bool, default False
    

whether to recursively add files in the input directory

See also

[`SparkContext.listFiles()`](pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles")
    
[`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")
    
[`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored.

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> from pyspark import SparkFiles
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="addFile") as d:
    ...     path1 = os.path.join(d, "test1.txt")
    ...     with open(path1, "w") as f:
    ...         _ = f.write("100")
    ...
    ...     path2 = os.path.join(d, "test2.txt")
    ...     with open(path2, "w") as f:
    ...         _ = f.write("200")
    ...
    ...     sc.addFile(path1)
    ...     file_list1 = sorted(sc.listFiles)
    ...
    ...     sc.addFile(path2)
    ...     file_list2 = sorted(sc.listFiles)
    ...
    ...     # add path2 twice, this addition will be ignored
    ...     sc.addFile(path2)
    ...     file_list3 = sorted(sc.listFiles)
    ...
    ...     def func(iterator):
    ...         with open(SparkFiles.get("test1.txt")) as f:
    ...             mul = int(f.readline())
    ...             return [x * mul for x in iterator]
    ...
    ...     collected = sc.parallelize([1, 2, 3, 4]).mapPartitions(func).collect()
    
    
    
    >>> file_list1
    ['file:/.../test1.txt']
    >>> file_list2
    ['file:/.../test1.txt', 'file:/.../test2.txt']
    >>> file_list3
    ['file:/.../test1.txt', 'file:/.../test2.txt']
    >>> collected
    [100, 200, 300, 400]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addFile.rst.txt)


---

## 🔹 059. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addJobTag.html

# pyspark.SparkContext.addJobTag#

SparkContext.addJobTag(_tag_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addJobTag)#
    

Add a tag to be assigned to all the jobs started by this thread.

Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group tag. The application can use [`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag") to cancel all running executions with this tag.

There may be multiple tags present at the same time, so different parts of application may use different tags to perform cancellation at different levels of granularity.

New in version 3.5.0.

Parameters
    

**tag** str
    

The tag to be added. Cannot contain â,â (comma) character.

See also

[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> import threading
    >>> from time import sleep
    >>> from pyspark import InheritableThread
    >>> sc.setInterruptOnCancel(interruptOnCancel=True)
    >>> result = "Not Set"
    >>> lock = threading.Lock()
    >>> def map_func(x):
    ...     sleep(100)
    ...     raise RuntimeError("Task should have been cancelled")
    ...
    >>> def start_job(x):
    ...     global result
    ...     try:
    ...         sc.addJobTag("job_to_cancel")
    ...         result = sc.parallelize(range(x)).map(map_func).collect()
    ...     except Exception as e:
    ...         result = "Cancelled"
    ...     lock.release()
    ...
    >>> def stop_job():
    ...     sleep(5)
    ...     sc.cancelJobsWithTag("job_to_cancel")
    ...
    >>> suppress = lock.acquire()
    >>> suppress = InheritableThread(target=start_job, args=(10,)).start()
    >>> suppress = InheritableThread(target=stop_job).start()
    >>> suppress = lock.acquire()
    >>> print(result)
    Cancelled
    >>> sc.clearJobTags()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addJobTag.rst.txt)


---

## 🔹 060. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.addPyFile.html

# pyspark.SparkContext.addPyFile#

SparkContext.addPyFile(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.addPyFile)#
    

Add a .py or .zip dependency for all tasks to be executed on this SparkContext in the future. The path passed can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI.

New in version 0.7.0.

Parameters
    

**path** str
    

can be either a .py file or .zip dependency.

See also

[`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")
    

Notes

A path can be added only once. Subsequent additions of the same path are ignored.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.addPyFile.rst.txt)


---

## 🔹 061. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.applicationId.html

# pyspark.SparkContext.applicationId#

_property _SparkContext.applicationId#
    

A unique identifier for the Spark application. Its format depends on the scheduler implementation.

  * in case of local spark app something like âlocal-1433865536131â

  * in case of YARN something like âapplication_1433865536131_34483â




New in version 1.5.0.

Examples
    
    
    >>> sc.applicationId  
    'local-...'
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.applicationId.rst.txt)


---

## 🔹 062. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.binaryFiles.html

# pyspark.SparkContext.binaryFiles#

SparkContext.binaryFiles(_path_ , _minPartitions =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.binaryFiles)#
    

Read a directory of binary files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI as a byte array. Each file is read as a single record and returned in a key-value pair, where the key is the path of each file, the value is the content of each file.

New in version 1.3.0.

Parameters
    

**path** str
    

directory to the input data files, the path can be comma separated paths as a list of inputs

**minPartitions** int, optional
    

suggested minimum number of partitions for the resulting RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD representing path-content pairs from the file(s).

See also

[`SparkContext.binaryRecords()`](pyspark.SparkContext.binaryRecords.html#pyspark.SparkContext.binaryRecords "pyspark.SparkContext.binaryRecords")
    

Notes

Small files are preferred, large file is also allowable, but may cause bad performance.

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="binaryFiles") as d:
    ...     # Write a temporary binary file
    ...     with open(os.path.join(d, "1.bin"), "wb") as f1:
    ...         _ = f1.write(b"binary data I")
    ...
    ...     # Write another temporary binary file
    ...     with open(os.path.join(d, "2.bin"), "wb") as f2:
    ...         _ = f2.write(b"binary data II")
    ...
    ...     collected = sorted(sc.binaryFiles(d).collect())
    
    
    
    >>> collected
    [('.../1.bin', b'binary data I'), ('.../2.bin', b'binary data II')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.binaryFiles.rst.txt)


---

## 🔹 063. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.binaryRecords.html

# pyspark.SparkContext.binaryRecords#

SparkContext.binaryRecords(_path_ , _recordLength_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.binaryRecords)#
    

Load data from a flat binary file, assuming each record is a set of numbers with the specified numerical format (see ByteBuffer), and the number of bytes per record is constant.

New in version 1.3.0.

Parameters
    

**path** str
    

Directory to the input data files

**recordLength** int
    

The length at which to split the records

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of data with values, represented as byte arrays

See also

[`SparkContext.binaryFiles()`](pyspark.SparkContext.binaryFiles.html#pyspark.SparkContext.binaryFiles "pyspark.SparkContext.binaryFiles")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="binaryRecords") as d:
    ...     # Write a temporary file
    ...     with open(os.path.join(d, "1.bin"), "w") as f:
    ...         for i in range(3):
    ...             _ = f.write("%04d" % i)
    ...
    ...     # Write another file
    ...     with open(os.path.join(d, "2.bin"), "w") as f:
    ...         for i in [-1, -2, -10]:
    ...             _ = f.write("%04d" % i)
    ...
    ...     collected = sorted(sc.binaryRecords(d, 4).collect())
    
    
    
    >>> collected
    [b'-001', b'-002', b'-010', b'0000', b'0001', b'0002']
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.binaryRecords.rst.txt)


---

## 🔹 064. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.broadcast.html

# pyspark.SparkContext.broadcast#

SparkContext.broadcast(_value_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.broadcast)#
    

Broadcast a read-only variable to the cluster, returning a [`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object for reading it in distributed functions. The variable will be sent to each cluster only once.

New in version 0.7.0.

Parameters
    

**value** T
    

value to broadcast to the Spark nodes

Returns
    

[`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast")
    

[`Broadcast`](pyspark.Broadcast.html#pyspark.Broadcast "pyspark.Broadcast") object, a read-only variable cached on each machine

Examples
    
    
    >>> mapping = {1: 10001, 2: 10002}
    >>> bc = sc.broadcast(mapping)
    
    
    
    >>> rdd = sc.range(5)
    >>> rdd2 = rdd.map(lambda i: bc.value[i] if i in bc.value else -1)
    >>> rdd2.collect()
    [-1, 10001, 10002, -1, -1]
    
    
    
    >>> bc.destroy()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.broadcast.rst.txt)


---

## 🔹 065. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelAllJobs.html

# pyspark.SparkContext.cancelAllJobs#

SparkContext.cancelAllJobs()[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelAllJobs)#
    

Cancel all jobs that have been scheduled or are running.

New in version 1.1.0.

See also

[`SparkContext.cancelJobGroup()`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.runJob()`](pyspark.SparkContext.runJob.html#pyspark.SparkContext.runJob "pyspark.SparkContext.runJob")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelAllJobs.rst.txt)


---

## 🔹 066. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelJobGroup.html

# pyspark.SparkContext.cancelJobGroup#

SparkContext.cancelJobGroup(_groupId_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelJobGroup)#
    

Cancel active jobs for the specified group. See [`SparkContext.setJobGroup()`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup"). for more information.

New in version 1.1.0.

Parameters
    

**groupId** str
    

The group ID to cancel the job.

See also

[`SparkContext.setJobGroup()`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelJobGroup.rst.txt)


---

## 🔹 067. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.cancelJobsWithTag.html

# pyspark.SparkContext.cancelJobsWithTag#

SparkContext.cancelJobsWithTag(_tag_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.cancelJobsWithTag)#
    

Cancel active jobs that have the specified tag. See [`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag").

New in version 3.5.0.

Parameters
    

**tag** str
    

The tag to be cancelled. Cannot contain â,â (comma) character.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.cancelJobsWithTag.rst.txt)


---

## 🔹 068. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.clearJobTags.html

# pyspark.SparkContext.clearJobTags#

SparkContext.clearJobTags()[[source]](../../_modules/pyspark/core/context.html#SparkContext.clearJobTags)#
    

Clear the current threadâs job tags.

New in version 3.5.0.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> sc.addJobTag("job_to_cancel")
    >>> sc.clearJobTags()
    >>> sc.getJobTags()
    set()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.clearJobTags.rst.txt)


---

## 🔹 069. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.defaultMinPartitions.html

# pyspark.SparkContext.defaultMinPartitions#

_property _SparkContext.defaultMinPartitions#
    

Default min number of partitions for Hadoop RDDs when not given by user

New in version 1.1.0.

Examples
    
    
    >>> sc.defaultMinPartitions > 0
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.defaultMinPartitions.rst.txt)


---

## 🔹 070. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.defaultParallelism.html

# pyspark.SparkContext.defaultParallelism#

_property _SparkContext.defaultParallelism#
    

Default level of parallelism to use when not given by user (e.g. for reduce tasks)

New in version 0.7.0.

Examples
    
    
    >>> sc.defaultParallelism > 0
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.defaultParallelism.rst.txt)


---

## 🔹 071. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.dump_profiles.html

# pyspark.SparkContext.dump_profiles#

SparkContext.dump_profiles(_path_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.dump_profiles)#
    

Dump the profile stats into directory path

New in version 1.2.0.

See also

[`SparkContext.show_profiles()`](pyspark.SparkContext.show_profiles.html#pyspark.SparkContext.show_profiles "pyspark.SparkContext.show_profiles")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.dump_profiles.rst.txt)


---

## 🔹 072. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.emptyRDD.html

# pyspark.SparkContext.emptyRDD#

SparkContext.emptyRDD()[[source]](../../_modules/pyspark/core/context.html#SparkContext.emptyRDD)#
    

Create an [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that has no partitions or elements.

New in version 1.5.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

An empty RDD

Examples
    
    
    >>> sc.emptyRDD()
    EmptyRDD...
    >>> sc.emptyRDD().count()
    0
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.emptyRDD.rst.txt)


---

## 🔹 073. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getCheckpointDir.html

# pyspark.SparkContext.getCheckpointDir#

SparkContext.getCheckpointDir()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getCheckpointDir)#
    

Return the directory where RDDs are checkpointed. Returns None if no checkpoint directory has been set.

New in version 3.1.0.

See also

[`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")
    
[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`RDD.getCheckpointFile()`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getCheckpointDir.rst.txt)


---

## 🔹 074. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getConf.html

# pyspark.SparkContext.getConf#

SparkContext.getConf()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getConf)#
    

Return a copy of this SparkContextâs configuration [`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf").

New in version 2.1.0.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getConf.rst.txt)


---

## 🔹 075. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getJobTags.html

# pyspark.SparkContext.getJobTags#

SparkContext.getJobTags()[[source]](../../_modules/pyspark/core/context.html#SparkContext.getJobTags)#
    

Get the tags that are currently set to be assigned to all the jobs started by this thread.

New in version 3.5.0.

Returns
    

set of str
    

the tags that are currently set to be assigned to all the jobs started by this thread.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> sc.addJobTag("job_to_cancel")
    >>> sc.getJobTags()
    {'job_to_cancel'}
    >>> sc.clearJobTags()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getJobTags.rst.txt)


---

## 🔹 076. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getLocalProperty.html

# pyspark.SparkContext.getLocalProperty#

SparkContext.getLocalProperty(_key_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getLocalProperty)#
    

Get a local property set in this thread, or null if it is missing. See [`setLocalProperty()`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty").

New in version 1.0.0.

See also

[`SparkContext.setLocalProperty()`](pyspark.SparkContext.setLocalProperty.html#pyspark.SparkContext.setLocalProperty "pyspark.SparkContext.setLocalProperty")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getLocalProperty.rst.txt)


---

## 🔹 077. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getOrCreate.html

# pyspark.SparkContext.getOrCreate#

_classmethod _SparkContext.getOrCreate(_conf =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getOrCreate)#
    

Get or instantiate a [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") and register it as a singleton object.

New in version 1.4.0.

Parameters
    

**conf**[` SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf"), optional
    

[`SparkConf`](pyspark.SparkConf.html#pyspark.SparkConf "pyspark.SparkConf") that will be used for initialization of the [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext").

Returns
    

[`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext")
    

current [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), or a new one if it wasnât created before the function call.

Examples
    
    
    >>> SparkContext.getOrCreate()
    <SparkContext ...>
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getOrCreate.rst.txt)


---

## 🔹 078. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.getSystemProperty.html

# pyspark.SparkContext.getSystemProperty#

_classmethod _SparkContext.getSystemProperty(_key_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.getSystemProperty)#
    

Get a Java system property, such as java.home.

New in version 4.0.0.

Parameters
    

**key** str
    

The key of a new Java system property.

Examples
    
    
    >>> sc.getSystemProperty("SPARK_SUBMIT")
    'true'
    >>> _ = sc.getSystemProperty("java.home")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.getSystemProperty.rst.txt)


---

## 🔹 079. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.hadoopFile.html

# pyspark.SparkContext.hadoopFile#

SparkContext.hadoopFile(_path_ , _inputFormatClass_ , _keyClass_ , _valueClass_ , _keyConverter =None_, _valueConverter =None_, _conf =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.hadoopFile)#
    

Read an âoldâ Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. The mechanism is the same as for meth:SparkContext.sequenceFile.

New in version 1.1.0.

A Hadoop configuration can be passed in as a Python dict. This will be converted into a Configuration in Java.

Parameters
    

**path** str
    

path to Hadoop file

**inputFormatClass** str
    

fully qualified classname of Hadoop InputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.input.TextInputFormatâ)

**keyClass** str
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter

**valueConverter** str, optional
    

fully qualified name of a function returning value WritableConverter

**conf** dict, optional
    

Hadoop configuration, passed in as a dict

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`SparkContext.newAPIHadoopFile()`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")
    
[`SparkContext.hadoopRDD()`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="hadoopFile") as d:
    ...     path = os.path.join(d, "old_hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsHadoopFile(path, output_format_class, key_class, value_class)
    ...
    ...     loaded = sc.hadoopFile(path, input_format_class, key_class, value_class)
    ...     collected = sorted(loaded.collect())
    
    
    
    >>> collected
    [(0, '1\t'), (0, '1\ta'), (0, '3\tx')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.hadoopFile.rst.txt)


---

## 🔹 080. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.hadoopRDD.html

# pyspark.SparkContext.hadoopRDD#

SparkContext.hadoopRDD(_inputFormatClass_ , _keyClass_ , _valueClass_ , _keyConverter =None_, _valueConverter =None_, _conf =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.hadoopRDD)#
    

Read an âoldâ Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict. This will be converted into a Configuration in Java. The mechanism is the same as for meth:SparkContext.sequenceFile.

New in version 1.1.0.

Parameters
    

**inputFormatClass** str
    

fully qualified classname of Hadoop InputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.input.TextInputFormatâ)

**keyClass** str
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter

**valueConverter** str, optional
    

fully qualified name of a function returning value WritableConverter

**conf** dict, optional
    

Hadoop configuration, passed in as a dict

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`SparkContext.newAPIHadoopRDD()`](pyspark.SparkContext.newAPIHadoopRDD.html#pyspark.SparkContext.newAPIHadoopRDD "pyspark.SparkContext.newAPIHadoopRDD")
    
[`SparkContext.hadoopFile()`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="hadoopRDD") as d:
    ...     path = os.path.join(d, "old_hadoop_file")
    ...
    ...     # Create the conf for writing
    ...     write_conf = {
    ...         "mapred.output.format.class": output_format_class,
    ...         "mapreduce.job.output.key.class": key_class,
    ...         "mapreduce.job.output.value.class": value_class,
    ...         "mapreduce.output.fileoutputformat.outputdir": path,
    ...     }
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsHadoopDataset(conf=write_conf)
    ...
    ...     # Create the conf for reading
    ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
    ...
    ...     loaded = sc.hadoopRDD(input_format_class, key_class, value_class, conf=read_conf)
    ...     collected = sorted(loaded.collect())
    
    
    
    >>> collected
    [(0, '1\t'), (0, '1\ta'), (0, '3\tx')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.hadoopRDD.rst.txt)


---

## 🔹 081. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.listArchives.html

# pyspark.SparkContext.listArchives#

_property _SparkContext.listArchives#
    

Returns a list of archive paths that are added to resources.

New in version 3.4.0.

See also

[`SparkContext.addArchive()`](pyspark.SparkContext.addArchive.html#pyspark.SparkContext.addArchive "pyspark.SparkContext.addArchive")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.listArchives.rst.txt)


---

## 🔹 082. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.listFiles.html

# pyspark.SparkContext.listFiles#

_property _SparkContext.listFiles#
    

Returns a list of file paths that are added to resources.

New in version 3.4.0.

See also

[`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.listFiles.rst.txt)


---

## 🔹 083. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.newAPIHadoopFile.html

# pyspark.SparkContext.newAPIHadoopFile#

SparkContext.newAPIHadoopFile(_path_ , _inputFormatClass_ , _keyClass_ , _valueClass_ , _keyConverter =None_, _valueConverter =None_, _conf =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.newAPIHadoopFile)#
    

Read a ânew APIâ Hadoop InputFormat with arbitrary key and value class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. The mechanism is the same as for meth:SparkContext.sequenceFile.

A Hadoop configuration can be passed in as a Python dict. This will be converted into a Configuration in Java

New in version 1.1.0.

Parameters
    

**path** str
    

path to Hadoop file

**inputFormatClass** str
    

fully qualified classname of Hadoop InputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.input.TextInputFormatâ)

**keyClass** str
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter None by default

**valueConverter** str, optional
    

fully qualified name of a function returning value WritableConverter None by default

**conf** dict, optional
    

Hadoop configuration, passed in as a dict None by default

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`SparkContext.sequenceFile()`](pyspark.SparkContext.sequenceFile.html#pyspark.SparkContext.sequenceFile "pyspark.SparkContext.sequenceFile")
    
[`SparkContext.hadoopFile()`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="newAPIHadoopFile") as d:
    ...     path = os.path.join(d, "new_hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsNewAPIHadoopFile(path, output_format_class, key_class, value_class)
    ...
    ...     loaded = sc.newAPIHadoopFile(path, input_format_class, key_class, value_class)
    ...     collected = sorted(loaded.collect())
    
    
    
    >>> collected
    [(1, ''), (1, 'a'), (3, 'x')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.newAPIHadoopFile.rst.txt)


---

## 🔹 084. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.newAPIHadoopRDD.html

# pyspark.SparkContext.newAPIHadoopRDD#

SparkContext.newAPIHadoopRDD(_inputFormatClass_ , _keyClass_ , _valueClass_ , _keyConverter =None_, _valueConverter =None_, _conf =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.newAPIHadoopRDD)#
    

Read a ânew APIâ Hadoop InputFormat with arbitrary key and value class, from an arbitrary Hadoop configuration, which is passed in as a Python dict. This will be converted into a Configuration in Java. The mechanism is the same as for meth:SparkContext.sequenceFile.

New in version 1.1.0.

Parameters
    

**inputFormatClass** str
    

fully qualified classname of Hadoop InputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.input.TextInputFormatâ)

**keyClass** str
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter (None by default)

**valueConverter** str, optional
    

fully qualified name of a function returning value WritableConverter (None by default)

**conf** dict, optional
    

Hadoop configuration, passed in as a dict (None by default)

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`SparkContext.hadoopRDD()`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")
    
[`SparkContext.hadoopFile()`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="newAPIHadoopRDD") as d:
    ...     path = os.path.join(d, "new_hadoop_file")
    ...
    ...     # Create the conf for writing
    ...     write_conf = {
    ...         "mapreduce.job.outputformat.class": (output_format_class),
    ...         "mapreduce.job.output.key.class": key_class,
    ...         "mapreduce.job.output.value.class": value_class,
    ...         "mapreduce.output.fileoutputformat.outputdir": path,
    ...     }
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsNewAPIHadoopDataset(conf=write_conf)
    ...
    ...     # Create the conf for reading
    ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
    ...
    ...     loaded = sc.newAPIHadoopRDD(input_format_class,
    ...         key_class, value_class, conf=read_conf)
    ...     collected = sorted(loaded.collect())
    
    
    
    >>> collected
    [(1, ''), (1, 'a'), (3, 'x')]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.newAPIHadoopRDD.rst.txt)


---

## 🔹 085. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.parallelize.html

# pyspark.SparkContext.parallelize#

SparkContext.parallelize(_c_ , _numSlices =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.parallelize)#
    

Distribute a local Python collection to form an RDD. Using range is recommended if the input represents a range for performance.

New in version 0.7.0.

Parameters
    

**c**` collections.abc.Iterable`
    

iterable collection to distribute

**numSlices** int, optional
    

the number of partitions of the new RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD representing distributed collection.

Examples
    
    
    >>> sc.parallelize([0, 2, 3, 4, 6], 5).glom().collect()
    [[0], [2], [3], [4], [6]]
    >>> sc.parallelize(range(0, 6, 2), 5).glom().collect()
    [[], [0], [], [2], [4]]
    

Deal with a list of strings.
    
    
    >>> strings = ["a", "b", "c"]
    >>> sc.parallelize(strings, 2).glom().collect()
    [['a'], ['b', 'c']]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.parallelize.rst.txt)


---

## 🔹 086. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.pickleFile.html

# pyspark.SparkContext.pickleFile#

SparkContext.pickleFile(_name_ , _minPartitions =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.pickleFile)#
    

Load an RDD previously saved using [`RDD.saveAsPickleFile()`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile") method.

New in version 1.1.0.

Parameters
    

**name** str
    

directory to the input data files, the path can be comma separated paths as a list of inputs

**minPartitions** int, optional
    

suggested minimum number of partitions for the resulting RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD representing unpickled data from the file(s).

See also

[`RDD.saveAsPickleFile()`](pyspark.RDD.saveAsPickleFile.html#pyspark.RDD.saveAsPickleFile "pyspark.RDD.saveAsPickleFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="pickleFile") as d:
    ...     # Write a temporary pickled file
    ...     path1 = os.path.join(d, "pickled1")
    ...     sc.parallelize(range(10)).saveAsPickleFile(path1, 3)
    ...
    ...     # Write another temporary pickled file
    ...     path2 = os.path.join(d, "pickled2")
    ...     sc.parallelize(range(-10, -5)).saveAsPickleFile(path2, 3)
    ...
    ...     # Load picked file
    ...     collected1 = sorted(sc.pickleFile(path1, 3).collect())
    ...     collected2 = sorted(sc.pickleFile(path2, 4).collect())
    ...
    ...     # Load two picked files together
    ...     collected3 = sorted(sc.pickleFile('{},{}'.format(path1, path2), 5).collect())
    
    
    
    >>> collected1
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> collected2
    [-10, -9, -8, -7, -6]
    >>> collected3
    [-10, -9, -8, -7, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.pickleFile.rst.txt)


---

## 🔹 087. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.range.html

# pyspark.SparkContext.range#

SparkContext.range(_start_ , _end =None_, _step =1_, _numSlices =None_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.range)#
    

Create a new RDD of int containing elements from start to end (exclusive), increased by step every element. Can be called the same way as pythonâs built-in range() function. If called with a single argument, the argument is interpreted as end, and start is set to 0.

New in version 1.5.0.

Parameters
    

**start** int
    

the start value

**end** int, optional
    

the end value (exclusive)

**step** int, optional, default 1
    

the incremental step

**numSlices** int, optional
    

the number of partitions of the new RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

An RDD of int

See also

[`pyspark.sql.SparkSession.range()`](../pyspark.sql/api/pyspark.sql.SparkSession.range.html#pyspark.sql.SparkSession.range "pyspark.sql.SparkSession.range")
    

Examples
    
    
    >>> sc.range(5).collect()
    [0, 1, 2, 3, 4]
    >>> sc.range(2, 4).collect()
    [2, 3]
    >>> sc.range(1, 7, 2).collect()
    [1, 3, 5]
    

Generate RDD with a negative step
    
    
    >>> sc.range(5, 0, -1).collect()
    [5, 4, 3, 2, 1]
    >>> sc.range(0, 5, -1).collect()
    []
    

Control the number of partitions
    
    
    >>> sc.range(5, numSlices=1).getNumPartitions()
    1
    >>> sc.range(5, numSlices=10).getNumPartitions()
    10
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.range.rst.txt)


---

## 🔹 088. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.resources.html

# pyspark.SparkContext.resources#

_property _SparkContext.resources#
    

Return the resource information of this [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"). A resource could be a GPU, FPGA, etc.

New in version 3.0.0.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.resources.rst.txt)


---

## 🔹 089. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.removeJobTag.html

# pyspark.SparkContext.removeJobTag#

SparkContext.removeJobTag(_tag_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.removeJobTag)#
    

Remove a tag previously added to be assigned to all the jobs started by this thread. Noop if such a tag was not added earlier.

New in version 3.5.0.

Parameters
    

**tag** str
    

The tag to be removed. Cannot contain â,â (comma) character.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.getJobTags()`](pyspark.SparkContext.getJobTags.html#pyspark.SparkContext.getJobTags "pyspark.SparkContext.getJobTags")
    
[`SparkContext.clearJobTags()`](pyspark.SparkContext.clearJobTags.html#pyspark.SparkContext.clearJobTags "pyspark.SparkContext.clearJobTags")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    
[`SparkContext.setInterruptOnCancel()`](pyspark.SparkContext.setInterruptOnCancel.html#pyspark.SparkContext.setInterruptOnCancel "pyspark.SparkContext.setInterruptOnCancel")
    

Examples
    
    
    >>> sc.addJobTag("job_to_cancel1")
    >>> sc.addJobTag("job_to_cancel2")
    >>> sc.getJobTags()
    {'job_to_cancel1', 'job_to_cancel2'}
    >>> sc.removeJobTag("job_to_cancel1")
    >>> sc.getJobTags()
    {'job_to_cancel2'}
    >>> sc.clearJobTags()
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.removeJobTag.rst.txt)


---

## 🔹 090. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.runJob.html

# pyspark.SparkContext.runJob#

SparkContext.runJob(_rdd_ , _partitionFunc_ , _partitions =None_, _allowLocal =False_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.runJob)#
    

Executes the given partitionFunc on the specified set of partitions, returning the result as an array of elements.

If âpartitionsâ is not specified, this will run over all partitions.

New in version 1.1.0.

Parameters
    

**rdd**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

target RDD to run tasks on

**partitionFunc** function
    

a function to run on each partition of the RDD

**partitions** list, optional
    

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like first

**allowLocal** bool, default False
    

this parameter takes no effect

Returns
    

list
    

results of specified partitions

See also

[`SparkContext.cancelAllJobs()`](pyspark.SparkContext.cancelAllJobs.html#pyspark.SparkContext.cancelAllJobs "pyspark.SparkContext.cancelAllJobs")
    

Examples
    
    
    >>> myRDD = sc.parallelize(range(6), 3)
    >>> sc.runJob(myRDD, lambda part: [x * x for x in part])
    [0, 1, 4, 9, 16, 25]
    
    
    
    >>> myRDD = sc.parallelize(range(6), 3)
    >>> sc.runJob(myRDD, lambda part: [x * x for x in part], [0, 2], True)
    [0, 1, 16, 25]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.runJob.rst.txt)


---

## 🔹 091. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.sequenceFile.html

# pyspark.SparkContext.sequenceFile#

SparkContext.sequenceFile(_path_ , _keyClass =None_, _valueClass =None_, _keyConverter =None_, _valueConverter =None_, _minSplits =None_, _batchSize =0_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.sequenceFile)#
    

Read a Hadoop SequenceFile with arbitrary key and value Writable class from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. The mechanism is as follows:

>   1. A Java RDD is created from the SequenceFile or other InputFormat, and the key and value Writable classes
> 
>   2. Serialization is attempted via Pickle pickling
> 
>   3. If this fails, the fallback is to call âtoStringâ on each key and value
> 
>   4. `CPickleSerializer` is used to deserialize pickled objects on the Python side
> 
> 


New in version 1.3.0.

Parameters
    

**path** str
    

path to sequencefile

**keyClass: str, optional**
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.Textâ)

**valueClass** str, optional
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.LongWritableâ)

**keyConverter** str, optional
    

fully qualified name of a function returning key WritableConverter

**valueConverter** str, optional
    

fully qualifiedname of a function returning value WritableConverter

**minSplits** int, optional
    

minimum splits in dataset (default min(2, sc.defaultParallelism))

**batchSize** int, optional, default 0
    

The number of Python objects represented as a single Java object. (default 0, choose batchSize automatically)

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

RDD of tuples of key and corresponding value

See also

[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`SparkContext.newAPIHadoopFile()`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")
    
[`SparkContext.hadoopFile()`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the class of output format
    
    
    >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="sequenceFile") as d:
    ...     path = os.path.join(d, "hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, {3.0: "bb"}), (2, {1.0: "aa"}), (3, {2.0: "dd"})])
    ...     rdd.saveAsNewAPIHadoopFile(path, output_format_class)
    ...
    ...     collected = sorted(sc.sequenceFile(path).collect())
    
    
    
    >>> collected
    [(1, {3.0: 'bb'}), (2, {1.0: 'aa'}), (3, {2.0: 'dd'})]
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.sequenceFile.rst.txt)


---

## 🔹 092. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setCheckpointDir.html

# pyspark.SparkContext.setCheckpointDir#

SparkContext.setCheckpointDir(_dirName_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setCheckpointDir)#
    

Set the directory under which RDDs are going to be checkpointed. The directory must be an HDFS path if running on a cluster.

New in version 0.7.0.

Parameters
    

**dirName** str
    

path to the directory where checkpoint files will be stored (must be HDFS path if running in cluster)

See also

[`SparkContext.getCheckpointDir()`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")
    
[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`RDD.getCheckpointFile()`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setCheckpointDir.rst.txt)


---

## 🔹 093. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setInterruptOnCancel.html

# pyspark.SparkContext.setInterruptOnCancel#

SparkContext.setInterruptOnCancel(_interruptOnCancel_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setInterruptOnCancel)#
    

Set the behavior of job cancellation from jobs started in this thread.

New in version 3.5.0.

Parameters
    

**interruptOnCancel** bool
    

If true, then job cancellation will result in `Thread.interrupt()` being called on the jobâs executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to `Thread.interrupt()` by marking nodes as dead.

See also

[`SparkContext.addJobTag()`](pyspark.SparkContext.addJobTag.html#pyspark.SparkContext.addJobTag "pyspark.SparkContext.addJobTag")
    
[`SparkContext.removeJobTag()`](pyspark.SparkContext.removeJobTag.html#pyspark.SparkContext.removeJobTag "pyspark.SparkContext.removeJobTag")
    
[`SparkContext.cancelAllJobs()`](pyspark.SparkContext.cancelAllJobs.html#pyspark.SparkContext.cancelAllJobs "pyspark.SparkContext.cancelAllJobs")
    
[`SparkContext.cancelJobGroup()`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")
    
[`SparkContext.cancelJobsWithTag()`](pyspark.SparkContext.cancelJobsWithTag.html#pyspark.SparkContext.cancelJobsWithTag "pyspark.SparkContext.cancelJobsWithTag")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setInterruptOnCancel.rst.txt)


---

## 🔹 094. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setJobDescription.html

# pyspark.SparkContext.setJobDescription#

SparkContext.setJobDescription(_value_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setJobDescription)#
    

Set a human readable description of the current job.

New in version 2.3.0.

Parameters
    

**value** str
    

The job description to set.

Notes

If you run jobs in parallel, use [`pyspark.InheritableThread`](pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread") for thread local inheritance.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setJobDescription.rst.txt)


---

## 🔹 095. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setJobGroup.html

# pyspark.SparkContext.setJobGroup#

SparkContext.setJobGroup(_groupId_ , _description_ , _interruptOnCancel =False_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setJobGroup)#
    

Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.

Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group description. Once set, the Spark web UI will associate such jobs with this group.

The application can use [`SparkContext.cancelJobGroup()`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup") to cancel all running jobs in this group.

New in version 1.0.0.

Parameters
    

**groupId** str
    

The group ID to assign.

**description** str
    

The description to set for the job group.

**interruptOnCancel** bool, optional, default False
    

whether to interrupt jobs on job cancellation.

See also

[`SparkContext.cancelJobGroup()`](pyspark.SparkContext.cancelJobGroup.html#pyspark.SparkContext.cancelJobGroup "pyspark.SparkContext.cancelJobGroup")
    

Notes

If interruptOnCancel is set to true for the job group, then job cancellation will result in Thread.interrupt() being called on the jobâs executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.

If you run jobs in parallel, use [`pyspark.InheritableThread`](pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread") for thread local inheritance.

Examples
    
    
    >>> import threading
    >>> from time import sleep
    >>> from pyspark import InheritableThread
    >>> result = "Not Set"
    >>> lock = threading.Lock()
    >>> def map_func(x):
    ...     sleep(100)
    ...     raise RuntimeError("Task should have been cancelled")
    ...
    >>> def start_job(x):
    ...     global result
    ...     try:
    ...         sc.setJobGroup("job_to_cancel", "some description")
    ...         result = sc.parallelize(range(x)).map(map_func).collect()
    ...     except Exception as e:
    ...         result = "Cancelled"
    ...     lock.release()
    ...
    >>> def stop_job():
    ...     sleep(5)
    ...     sc.cancelJobGroup("job_to_cancel")
    ...
    >>> suppress = lock.acquire()
    >>> suppress = InheritableThread(target=start_job, args=(10,)).start()
    >>> suppress = InheritableThread(target=stop_job).start()
    >>> suppress = lock.acquire()
    >>> print(result)
    Cancelled
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setJobGroup.rst.txt)


---

## 🔹 096. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setLocalProperty.html

# pyspark.SparkContext.setLocalProperty#

SparkContext.setLocalProperty(_key_ , _value_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setLocalProperty)#
    

Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.

To remove/unset property simply set value to None e.g. sc.setLocalProperty(âkeyâ, None)

New in version 1.0.0.

Parameters
    

**key** str
    

The key of the local property to set.

**value** str
    

The value of the local property to set. If set to None then the property will be removed

See also

[`SparkContext.getLocalProperty()`](pyspark.SparkContext.getLocalProperty.html#pyspark.SparkContext.getLocalProperty "pyspark.SparkContext.getLocalProperty")
    

Notes

If you run jobs in parallel, use [`pyspark.InheritableThread`](pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread") for thread local inheritance.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setLocalProperty.rst.txt)


---

## 🔹 097. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setLogLevel.html

# pyspark.SparkContext.setLogLevel#

SparkContext.setLogLevel(_logLevel_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setLogLevel)#
    

Control our logLevel. This overrides any user-defined log settings. Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN

New in version 1.4.0.

Parameters
    

**logLevel** str
    

The desired log level as a string.

Examples
    
    
    >>> sc.setLogLevel("WARN")  # doctest :+SKIP
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setLogLevel.rst.txt)


---

## 🔹 098. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.setSystemProperty.html

# pyspark.SparkContext.setSystemProperty#

_classmethod _SparkContext.setSystemProperty(_key_ , _value_)[[source]](../../_modules/pyspark/core/context.html#SparkContext.setSystemProperty)#
    

Set a Java system property, such as spark.executor.memory. This must be invoked before instantiating [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext").

New in version 0.9.0.

Parameters
    

**key** str
    

The key of a new Java system property.

**value** str
    

The value of a new Java system property.

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.setSystemProperty.rst.txt)


---

## 🔹 099. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.show_profiles.html

# pyspark.SparkContext.show_profiles#

SparkContext.show_profiles()[[source]](../../_modules/pyspark/core/context.html#SparkContext.show_profiles)#
    

Print the profile stats to stdout

New in version 1.2.0.

See also

[`SparkContext.dump_profiles()`](pyspark.SparkContext.dump_profiles.html#pyspark.SparkContext.dump_profiles "pyspark.SparkContext.dump_profiles")
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkContext.show_profiles.rst.txt)


---

## 🔹 100. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.aggregate.html

# pyspark.RDD.aggregate#

RDD.aggregate(_zeroValue_ , _seqOp_ , _combOp_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.aggregate)#
    

Aggregate the elements of each partition, and then the results for all the partitions, using a given combine functions and a neutral âzero value.â

The functions `op(t1, t2)` is allowed to modify `t1` and return it as its result value to avoid object allocation; however, it should not modify `t2`.

The first function (seqOp) can return a different result type, U, than the type of this RDD. Thus, we need one operation for merging a T into an U and one operation for merging two U

New in version 1.1.0.

Parameters
    

**zeroValue** U
    

the initial value for the accumulated result of each partition

**seqOp** function
    

a function used to accumulate results within a partition

**combOp** function
    

an associative function used to combine results from different partitions

Returns
    

U
    

the aggregated result

See also

[`RDD.reduce()`](pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")
    
[`RDD.fold()`](pyspark.RDD.fold.html#pyspark.RDD.fold "pyspark.RDD.fold")
    

Examples
    
    
    >>> seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
    >>> combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
    >>> sc.parallelize([1, 2, 3, 4]).aggregate((0, 0), seqOp, combOp)
    (10, 4)
    >>> sc.parallelize([]).aggregate((0, 0), seqOp, combOp)
    (0, 0)
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.aggregate.rst.txt)


---

## 🔹 101. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.aggregateByKey.html

# pyspark.RDD.aggregateByKey#

RDD.aggregateByKey(_zeroValue_ , _seqFunc_ , _combFunc_ , _numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.aggregateByKey)#
    

Aggregate the values of each key, using given combine functions and a neutral âzero valueâ. This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two Uâs, The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U.

New in version 1.1.0.

Parameters
    

**zeroValue** U
    

the initial value for the accumulated result of each partition

**seqFunc** function
    

a function to merge a V into a U

**combFunc** function
    

a function to combine two Uâs into a single one

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the aggregated result for each key

See also

[`RDD.reduceByKey()`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")
    
[`RDD.combineByKey()`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")
    
[`RDD.foldByKey()`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")
    
[`RDD.groupByKey()`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")
    

Examples
    
    
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 2)])
    >>> seqFunc = (lambda x, y: (x[0] + y, x[1] + 1))
    >>> combFunc = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
    >>> sorted(rdd.aggregateByKey((0, 0), seqFunc, combFunc).collect())
    [('a', (3, 2)), ('b', (1, 1))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.aggregateByKey.rst.txt)


---

## 🔹 102. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.barrier.html

# pyspark.RDD.barrier#

RDD.barrier()[[source]](../../_modules/pyspark/core/rdd.html#RDD.barrier)#
    

Marks the current stage as a barrier stage, where Spark must launch all tasks together. In case of a task failure, instead of only restarting the failed task, Spark will abort the entire stage and relaunch all tasks for this stage. The barrier execution mode feature is experimental and it only handles limited scenarios. Please read the linked SPIP and design docs to understand the limitations and future plans.

New in version 2.4.0.

Returns
    

[`RDDBarrier`](pyspark.RDDBarrier.html#pyspark.RDDBarrier "pyspark.RDDBarrier")
    

instance that provides actions within a barrier stage.

See also

[`pyspark.BarrierTaskContext`](pyspark.BarrierTaskContext.html#pyspark.BarrierTaskContext "pyspark.BarrierTaskContext")
    

Notes

For additional information see

  * [SPIP: Barrier Execution Mode](https://issues.apache.org/jira/browse/SPARK-24374)

  * [Design Doc](https://issues.apache.org/jira/browse/SPARK-24582)




This API is experimental

[ __Show Source](../../_sources/reference/api/pyspark.RDD.barrier.rst.txt)


---

## 🔹 103. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.cache.html

# pyspark.RDD.cache#

RDD.cache()[[source]](../../_modules/pyspark/core/rdd.html#RDD.cache)#
    

Persist this RDD with the default storage level (MEMORY_ONLY).

New in version 0.7.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

The same [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with storage level set to MEMORY_ONLY

See also

[`RDD.persist()`](pyspark.RDD.persist.html#pyspark.RDD.persist "pyspark.RDD.persist")
    
[`RDD.unpersist()`](pyspark.RDD.unpersist.html#pyspark.RDD.unpersist "pyspark.RDD.unpersist")
    
[`RDD.getStorageLevel()`](pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")
    

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd2 = rdd.cache()
    >>> rdd2 is rdd
    True
    >>> str(rdd.getStorageLevel())
    'Memory Serialized 1x Replicated'
    >>> _ = rdd.unpersist()
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.cache.rst.txt)


---

## 🔹 104. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.cartesian.html

# pyspark.RDD.cartesian#

RDD.cartesian(_other_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.cartesian)#
    

Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements `(a, b)` where `a` is in self and `b` is in other.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

the Cartesian product of this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") and another one

See also

[`pyspark.sql.DataFrame.crossJoin()`](../pyspark.sql/api/pyspark.sql.DataFrame.crossJoin.html#pyspark.sql.DataFrame.crossJoin "pyspark.sql.DataFrame.crossJoin")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2])
    >>> sorted(rdd.cartesian(rdd).collect())
    [(1, 1), (1, 2), (2, 1), (2, 2)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.cartesian.rst.txt)


---

## 🔹 105. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.checkpoint.html

# pyspark.RDD.checkpoint#

RDD.checkpoint()[[source]](../../_modules/pyspark/core/rdd.html#RDD.checkpoint)#
    

Mark this RDD for checkpointing. It will be saved to a file inside the checkpoint directory set with [`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir") and all references to its parent RDDs will be removed. This function must be called before any job has been executed on this RDD. It is strongly recommended that this RDD is persisted in memory, otherwise saving it on a file will require recomputation.

New in version 0.7.0.

See also

[`RDD.isCheckpointed()`](pyspark.RDD.isCheckpointed.html#pyspark.RDD.isCheckpointed "pyspark.RDD.isCheckpointed")
    
[`RDD.getCheckpointFile()`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")
    
[`RDD.localCheckpoint()`](pyspark.RDD.localCheckpoint.html#pyspark.RDD.localCheckpoint "pyspark.RDD.localCheckpoint")
    
[`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")
    
[`SparkContext.getCheckpointDir()`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")
    

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.is_checkpointed
    False
    >>> rdd.getCheckpointFile() == None
    True
    
    
    
    >>> rdd.checkpoint()
    >>> rdd.is_checkpointed
    True
    >>> rdd.getCheckpointFile() == None
    True
    
    
    
    >>> rdd.count()
    5
    >>> rdd.is_checkpointed
    True
    >>> rdd.getCheckpointFile() == None
    False
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.checkpoint.rst.txt)


---

## 🔹 106. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.cleanShuffleDependencies.html

# pyspark.RDD.cleanShuffleDependencies#

RDD.cleanShuffleDependencies(_blocking =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.cleanShuffleDependencies)#
    

Removes an RDDâs shuffles and itâs non-persisted ancestors.

When running without a shuffle service, cleaning up shuffle files enables downscaling. If you use the RDD after this call, you should checkpoint and materialize it first.

New in version 3.3.0.

Parameters
    

**blocking** bool, optional, default False
    

whether to block on shuffle cleanup tasks

Notes

This API is a developer API.

[ __Show Source](../../_sources/reference/api/pyspark.RDD.cleanShuffleDependencies.rst.txt)


---

## 🔹 107. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.coalesce.html

# pyspark.RDD.coalesce#

RDD.coalesce(_numPartitions_ , _shuffle =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.coalesce)#
    

Return a new RDD that is reduced into numPartitions partitions.

New in version 1.0.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**shuffle** bool, optional, default False
    

whether to add a shuffle step

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") that is reduced into numPartitions partitions

See also

[`RDD.repartition()`](pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3, 4, 5], 3).glom().collect()
    [[1], [2, 3], [4, 5]]
    >>> sc.parallelize([1, 2, 3, 4, 5], 3).coalesce(1).glom().collect()
    [[1, 2, 3, 4, 5]]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.coalesce.rst.txt)


---

## 🔹 108. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.cogroup.html

# pyspark.RDD.cogroup#

RDD.cogroup(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.cogroup)#
    

For each key k in self or other, return a resulting RDD that contains a tuple with the list of values for that key in self as well as other.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and cogrouped values

See also

[`RDD.groupWith()`](pyspark.RDD.groupWith.html#pyspark.RDD.groupWith "pyspark.RDD.groupWith")
    
[`RDD.join()`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd2 = sc.parallelize([("a", 2)])
    >>> [(x, tuple(map(list, y))) for x, y in sorted(list(rdd1.cogroup(rdd2).collect()))]
    [('a', ([1], [2])), ('b', ([4], []))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.cogroup.rst.txt)


---

## 🔹 109. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.collect.html

# pyspark.RDD.collect#

RDD.collect()[[source]](../../_modules/pyspark/core/rdd.html#RDD.collect)#
    

Return a list that contains all the elements in this RDD.

New in version 0.7.0.

Returns
    

list
    

a list containing all the elements

See also

[`RDD.toLocalIterator()`](pyspark.RDD.toLocalIterator.html#pyspark.RDD.toLocalIterator "pyspark.RDD.toLocalIterator")
    
[`pyspark.sql.DataFrame.collect()`](../pyspark.sql/api/pyspark.sql.DataFrame.collect.html#pyspark.sql.DataFrame.collect "pyspark.sql.DataFrame.collect")
    

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driverâs memory.

Examples
    
    
    >>> sc.range(5).collect()
    [0, 1, 2, 3, 4]
    >>> sc.parallelize(["x", "y", "z"]).collect()
    ['x', 'y', 'z']
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.collect.rst.txt)


---

## 🔹 110. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.collectAsMap.html

# pyspark.RDD.collectAsMap#

RDD.collectAsMap()[[source]](../../_modules/pyspark/core/rdd.html#RDD.collectAsMap)#
    

Return the key-value pairs in this RDD to the master as a dictionary.

New in version 0.7.0.

Returns
    

`dict`
    

a dictionary of (key, value) pairs

See also

[`RDD.countByValue()`](pyspark.RDD.countByValue.html#pyspark.RDD.countByValue "pyspark.RDD.countByValue")
    

Notes

This method should only be used if the resulting data is expected to be small, as all the data is loaded into the driverâs memory.

Examples
    
    
    >>> m = sc.parallelize([(1, 2), (3, 4)]).collectAsMap()
    >>> m[1]
    2
    >>> m[3]
    4
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.collectAsMap.rst.txt)


---

## 🔹 111. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.collectWithJobGroup.html

# pyspark.RDD.collectWithJobGroup#

RDD.collectWithJobGroup(_groupId_ , _description_ , _interruptOnCancel =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.collectWithJobGroup)#
    

When collect rdd, use this method to specify job group.

New in version 3.0.0.

Deprecated since version 3.1.0: Use [`pyspark.InheritableThread`](pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread") with the pinned thread mode enabled.

Parameters
    

**groupId** str
    

The group ID to assign.

**description** str
    

The description to set for the job group.

**interruptOnCancel** bool, optional, default False
    

whether to interrupt jobs on job cancellation.

Returns
    

list
    

a list containing all the elements

See also

[`RDD.collect()`](pyspark.RDD.collect.html#pyspark.RDD.collect "pyspark.RDD.collect")
    
[`SparkContext.setJobGroup()`](pyspark.SparkContext.setJobGroup.html#pyspark.SparkContext.setJobGroup "pyspark.SparkContext.setJobGroup")
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.collectWithJobGroup.rst.txt)


---

## 🔹 112. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.combineByKey.html

# pyspark.RDD.combineByKey#

RDD.combineByKey(_createCombiner_ , _mergeValue_ , _mergeCombiners_ , _numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.combineByKey)#
    

Generic function to combine the elements for each key using a custom set of aggregation functions.

Turns an RDD[(K, V)] into a result of type RDD[(K, C)], for a âcombined typeâ C.

To avoid memory allocation, both mergeValue and mergeCombiners are allowed to modify and return their first argument instead of creating a new C.

In addition, users can control the partitioning of the output RDD.

New in version 0.7.0.

Parameters
    

**createCombiner** function
    

a function to turns a V into a C

**mergeValue** function
    

a function to merge a V into a C

**mergeCombiners** function
    

a function to combine two Câs into a single one

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the aggregated result for each key

See also

[`RDD.reduceByKey()`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")
    
[`RDD.aggregateByKey()`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")
    
[`RDD.foldByKey()`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")
    
[`RDD.groupByKey()`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")
    

Notes

V and C can be different â for example, one might group an RDD of type
    

(Int, Int) into an RDD of type (Int, List[Int]).

Examples
    
    
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 2)])
    >>> def to_list(a):
    ...     return [a]
    ...
    >>> def append(a, b):
    ...     a.append(b)
    ...     return a
    ...
    >>> def extend(a, b):
    ...     a.extend(b)
    ...     return a
    ...
    >>> sorted(rdd.combineByKey(to_list, append, extend).collect())
    [('a', [1, 2]), ('b', [1])]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.combineByKey.rst.txt)


---

## 🔹 113. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.context.html

# pyspark.RDD.context#

_property _RDD.context#
    

The [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") that this RDD was created on.

New in version 0.7.0.

Returns
    

[`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext")
    

The [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext") that this RDD was created on

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.context
    <SparkContext ...>
    >>> rdd.context is sc
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.context.rst.txt)


---

## 🔹 114. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.count.html

# pyspark.RDD.count#

RDD.count()[[source]](../../_modules/pyspark/core/rdd.html#RDD.count)#
    

Return the number of elements in this RDD.

New in version 0.7.0.

Returns
    

int
    

the number of elements

See also

[`RDD.countApprox()`](pyspark.RDD.countApprox.html#pyspark.RDD.countApprox "pyspark.RDD.countApprox")
    
[`pyspark.sql.DataFrame.count()`](../pyspark.sql/api/pyspark.sql.DataFrame.count.html#pyspark.sql.DataFrame.count "pyspark.sql.DataFrame.count")
    

Examples
    
    
    >>> sc.parallelize([2, 3, 4]).count()
    3
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.count.rst.txt)


---

## 🔹 115. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.countApprox.html

# pyspark.RDD.countApprox#

RDD.countApprox(_timeout_ , _confidence =0.95_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.countApprox)#
    

Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.

New in version 1.2.0.

Parameters
    

**timeout** int
    

maximum time to wait for the job, in milliseconds

**confidence** float
    

the desired statistical confidence in the result

Returns
    

int
    

a potentially incomplete result, with error bounds

See also

[`RDD.count()`](pyspark.RDD.count.html#pyspark.RDD.count "pyspark.RDD.count")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(1000), 10)
    >>> rdd.countApprox(1000, 1.0)
    1000
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.countApprox.rst.txt)


---

## 🔹 116. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.countApproxDistinct.html

# pyspark.RDD.countApproxDistinct#

RDD.countApproxDistinct(_relativeSD =0.05_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.countApproxDistinct)#
    

Return approximate number of distinct elements in the RDD.

New in version 1.2.0.

Parameters
    

**relativeSD** float, optional
    

Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017.

Returns
    

int
    

approximate number of distinct elements

See also

[`RDD.distinct()`](pyspark.RDD.distinct.html#pyspark.RDD.distinct "pyspark.RDD.distinct")
    

Notes

The algorithm used is based on streamlibâs implementation of [âHyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithmâ, available here](https://doi.org/10.1145/2452376.2452456).

Examples
    
    
    >>> n = sc.parallelize(range(1000)).map(str).countApproxDistinct()
    >>> 900 < n < 1100
    True
    >>> n = sc.parallelize([i % 20 for i in range(1000)]).countApproxDistinct()
    >>> 16 < n < 24
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.countApproxDistinct.rst.txt)


---

## 🔹 117. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.countByKey.html

# pyspark.RDD.countByKey#

RDD.countByKey()[[source]](../../_modules/pyspark/core/rdd.html#RDD.countByKey)#
    

Count the number of elements for each key, and return the result to the master as a dictionary.

New in version 0.7.0.

Returns
    

dict
    

a dictionary of (key, count) pairs

See also

[`RDD.collectAsMap()`](pyspark.RDD.collectAsMap.html#pyspark.RDD.collectAsMap "pyspark.RDD.collectAsMap")
    
[`RDD.countByValue()`](pyspark.RDD.countByValue.html#pyspark.RDD.countByValue "pyspark.RDD.countByValue")
    

Examples
    
    
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
    >>> sorted(rdd.countByKey().items())
    [('a', 2), ('b', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.countByKey.rst.txt)


---

## 🔹 118. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.countByValue.html

# pyspark.RDD.countByValue#

RDD.countByValue()[[source]](../../_modules/pyspark/core/rdd.html#RDD.countByValue)#
    

Return the count of each unique value in this RDD as a dictionary of (value, count) pairs.

New in version 0.7.0.

Returns
    

dict
    

a dictionary of (value, count) pairs

See also

[`RDD.collectAsMap()`](pyspark.RDD.collectAsMap.html#pyspark.RDD.collectAsMap "pyspark.RDD.collectAsMap")
    
[`RDD.countByKey()`](pyspark.RDD.countByKey.html#pyspark.RDD.countByKey "pyspark.RDD.countByKey")
    

Examples
    
    
    >>> sorted(sc.parallelize([1, 2, 1, 2, 2], 2).countByValue().items())
    [(1, 2), (2, 3)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.countByValue.rst.txt)


---

## 🔹 119. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.distinct.html

# pyspark.RDD.distinct#

RDD.distinct(_numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.distinct)#
    

Return a new RDD containing the distinct elements in this RDD.

New in version 0.7.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the distinct elements

See also

[`RDD.countApproxDistinct()`](pyspark.RDD.countApproxDistinct.html#pyspark.RDD.countApproxDistinct "pyspark.RDD.countApproxDistinct")
    

Examples
    
    
    >>> sorted(sc.parallelize([1, 1, 2, 3]).distinct().collect())
    [1, 2, 3]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.distinct.rst.txt)


---

## 🔹 120. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.filter.html

# pyspark.RDD.filter#

RDD.filter(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.filter)#
    

Return a new RDD containing only the elements that satisfy a predicate.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to run on each element of the RDD

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each element

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4, 5])
    >>> rdd.filter(lambda x: x % 2 == 0).collect()
    [2, 4]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.filter.rst.txt)


---

## 🔹 121. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.first.html

# pyspark.RDD.first#

RDD.first()[[source]](../../_modules/pyspark/core/rdd.html#RDD.first)#
    

Return the first element in this RDD.

New in version 0.7.0.

Returns
    

T
    

the first element

See also

[`RDD.take()`](pyspark.RDD.take.html#pyspark.RDD.take "pyspark.RDD.take")
    
[`pyspark.sql.DataFrame.first()`](../pyspark.sql/api/pyspark.sql.DataFrame.first.html#pyspark.sql.DataFrame.first "pyspark.sql.DataFrame.first")
    
[`pyspark.sql.DataFrame.head()`](../pyspark.sql/api/pyspark.sql.DataFrame.head.html#pyspark.sql.DataFrame.head "pyspark.sql.DataFrame.head")
    

Examples
    
    
    >>> sc.parallelize([2, 3, 4]).first()
    2
    >>> sc.parallelize([]).first()
    Traceback (most recent call last):
        ...
    ValueError: RDD is empty
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.first.rst.txt)


---

## 🔹 122. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.flatMap.html

# pyspark.RDD.flatMap#

RDD.flatMap(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.flatMap)#
    

Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to turn a T into a sequence of U

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to all elements

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")
    
[`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")
    
[`RDD.mapPartitionsWithSplit()`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")
    

Examples
    
    
    >>> rdd = sc.parallelize([2, 3, 4])
    >>> sorted(rdd.flatMap(lambda x: range(1, x)).collect())
    [1, 1, 1, 2, 2, 3]
    >>> sorted(rdd.flatMap(lambda x: [(x, x), (x, x)]).collect())
    [(2, 2), (2, 2), (3, 3), (3, 3), (4, 4), (4, 4)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.flatMap.rst.txt)


---

## 🔹 123. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.flatMapValues.html

# pyspark.RDD.flatMapValues#

RDD.flatMapValues(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.flatMapValues)#
    

Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDDâs partitioning.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to turn a V into a sequence of U

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the flat-mapped value

See also

[`RDD.flatMap()`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")
    
[`RDD.mapValues()`](pyspark.RDD.mapValues.html#pyspark.RDD.mapValues "pyspark.RDD.mapValues")
    

Examples
    
    
    >>> rdd = sc.parallelize([("a", ["x", "y", "z"]), ("b", ["p", "r"])])
    >>> def f(x): return x
    ...
    >>> rdd.flatMapValues(f).collect()
    [('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.flatMapValues.rst.txt)


---

## 🔹 124. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.fold.html

# pyspark.RDD.fold#

RDD.fold(_zeroValue_ , _op_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.fold)#
    

Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral âzero value.â

The function `op(t1, t2)` is allowed to modify `t1` and return it as its result value to avoid object allocation; however, it should not modify `t2`.

This behaves somewhat differently from fold operations implemented for non-distributed collections in functional languages like Scala. This fold operation may be applied to partitions individually, and then fold those results into the final result, rather than apply the fold to each element sequentially in some defined ordering. For functions that are not commutative, the result may differ from that of a fold applied to a non-distributed collection.

New in version 0.7.0.

Parameters
    

**zeroValue** T
    

the initial value for the accumulated result of each partition

**op** function
    

a function used to both accumulate results within a partition and combine results from different partitions

Returns
    

T
    

the aggregated result

See also

[`RDD.reduce()`](pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")
    
[`RDD.aggregate()`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")
    

Examples
    
    
    >>> from operator import add
    >>> sc.parallelize([1, 2, 3, 4, 5]).fold(0, add)
    15
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.fold.rst.txt)


---

## 🔹 125. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.foldByKey.html

# pyspark.RDD.foldByKey#

RDD.foldByKey(_zeroValue_ , _func_ , _numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.foldByKey)#
    

Merge the values for each key using an associative function âfuncâ and a neutral âzeroValueâ which may be added to the result an arbitrary number of times, and must not change the result (e.g., 0 for addition, or 1 for multiplication.).

New in version 1.1.0.

Parameters
    

**zeroValue** V
    

the initial value for the accumulated result of each partition

**func** function
    

a function to combine two Vâs into a single one

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the aggregated result for each key

See also

[`RDD.reduceByKey()`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")
    
[`RDD.combineByKey()`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")
    
[`RDD.aggregateByKey()`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")
    
[`RDD.groupByKey()`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")
    

Examples
    
    
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
    >>> from operator import add
    >>> sorted(rdd.foldByKey(0, add).collect())
    [('a', 2), ('b', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.foldByKey.rst.txt)


---

## 🔹 126. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.foreach.html

# pyspark.RDD.foreach#

RDD.foreach(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.foreach)#
    

Applies a function to all elements of this RDD.

New in version 0.7.0.

Parameters
    

**f** function
    

a function applied to each element

See also

[`RDD.foreachPartition()`](pyspark.RDD.foreachPartition.html#pyspark.RDD.foreachPartition "pyspark.RDD.foreachPartition")
    
[`pyspark.sql.DataFrame.foreach()`](../pyspark.sql/api/pyspark.sql.DataFrame.foreach.html#pyspark.sql.DataFrame.foreach "pyspark.sql.DataFrame.foreach")
    
[`pyspark.sql.DataFrame.foreachPartition()`](../pyspark.sql/api/pyspark.sql.DataFrame.foreachPartition.html#pyspark.sql.DataFrame.foreachPartition "pyspark.sql.DataFrame.foreachPartition")
    

Examples
    
    
    >>> def f(x): print(x)
    ...
    >>> sc.parallelize([1, 2, 3, 4, 5]).foreach(f)
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.foreach.rst.txt)


---

## 🔹 127. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.foreachPartition.html

# pyspark.RDD.foreachPartition#

RDD.foreachPartition(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.foreachPartition)#
    

Applies a function to each partition of this RDD.

New in version 1.0.0.

Parameters
    

**f** function
    

a function applied to each partition

See also

[`RDD.foreach()`](pyspark.RDD.foreach.html#pyspark.RDD.foreach "pyspark.RDD.foreach")
    
[`pyspark.sql.DataFrame.foreach()`](../pyspark.sql/api/pyspark.sql.DataFrame.foreach.html#pyspark.sql.DataFrame.foreach "pyspark.sql.DataFrame.foreach")
    
[`pyspark.sql.DataFrame.foreachPartition()`](../pyspark.sql/api/pyspark.sql.DataFrame.foreachPartition.html#pyspark.sql.DataFrame.foreachPartition "pyspark.sql.DataFrame.foreachPartition")
    

Examples
    
    
    >>> def f(iterator):
    ...     for x in iterator:
    ...          print(x)
    ...
    >>> sc.parallelize([1, 2, 3, 4, 5]).foreachPartition(f)
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.foreachPartition.rst.txt)


---

## 🔹 128. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.fullOuterJoin.html

# pyspark.RDD.fullOuterJoin#

RDD.fullOuterJoin(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.fullOuterJoin)#
    

Perform a right outer join of self and other.

For each element (k, v) in self, the resulting RDD will either contain all pairs (k, (v, w)) for w in other, or the pair (k, (v, None)) if no elements in other have key k.

Similarly, for each element (k, w) in other, the resulting RDD will either contain all pairs (k, (v, w)) for v in self, or the pair (k, (None, w)) if no elements in self have key k.

Hash-partitions the resulting RDD into the given number of partitions.

New in version 1.2.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing all pairs of elements with matching keys

See also

[`RDD.join()`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")
    
[`RDD.leftOuterJoin()`](pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")
    
`RDD.fullOuterJoin()`
    
[`pyspark.sql.DataFrame.join()`](../pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join "pyspark.sql.DataFrame.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd2 = sc.parallelize([("a", 2), ("c", 8)])
    >>> sorted(rdd1.fullOuterJoin(rdd2).collect())
    [('a', (1, 2)), ('b', (4, None)), ('c', (None, 8))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.fullOuterJoin.rst.txt)


---

## 🔹 129. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.getCheckpointFile.html

# pyspark.RDD.getCheckpointFile#

RDD.getCheckpointFile()[[source]](../../_modules/pyspark/core/rdd.html#RDD.getCheckpointFile)#
    

Gets the name of the file to which this RDD was checkpointed

Not defined if RDD is checkpointed locally.

New in version 0.7.0.

Returns
    

str
    

the name of the file to which this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") was checkpointed

See also

[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")
    
[`SparkContext.getCheckpointDir()`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.getCheckpointFile.rst.txt)


---

## 🔹 130. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.getNumPartitions.html

# pyspark.RDD.getNumPartitions#

RDD.getNumPartitions()[[source]](../../_modules/pyspark/core/rdd.html#RDD.getNumPartitions)#
    

Returns the number of partitions in RDD

New in version 1.1.0.

Returns
    

int
    

number of partitions

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 2)
    >>> rdd.getNumPartitions()
    2
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.getNumPartitions.rst.txt)


---

## 🔹 131. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.getResourceProfile.html

# pyspark.RDD.getResourceProfile#

RDD.getResourceProfile()[[source]](../../_modules/pyspark/core/rdd.html#RDD.getResourceProfile)#
    

Get the [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") specified with this RDD or None if it wasnât specified.

New in version 3.1.0.

Returns
    

class:pyspark.resource.ResourceProfile
    

The user specified profile or None if none were specified

See also

[`RDD.withResources()`](pyspark.RDD.withResources.html#pyspark.RDD.withResources "pyspark.RDD.withResources")
    

Notes

This API is experimental

[ __Show Source](../../_sources/reference/api/pyspark.RDD.getResourceProfile.rst.txt)


---

## 🔹 132. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.getStorageLevel.html

# pyspark.RDD.getStorageLevel#

RDD.getStorageLevel()[[source]](../../_modules/pyspark/core/rdd.html#RDD.getStorageLevel)#
    

Get the RDDâs current storage level.

New in version 1.0.0.

Returns
    

[`StorageLevel`](pyspark.StorageLevel.html#pyspark.StorageLevel "pyspark.StorageLevel")
    

current [`StorageLevel`](pyspark.StorageLevel.html#pyspark.StorageLevel "pyspark.StorageLevel")

See also

[`RDD.name()`](pyspark.RDD.name.html#pyspark.RDD.name "pyspark.RDD.name")
    

Examples
    
    
    >>> rdd = sc.parallelize([1,2])
    >>> rdd.getStorageLevel()
    StorageLevel(False, False, False, False, 1)
    >>> print(rdd.getStorageLevel())
    Serialized 1x Replicated
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.getStorageLevel.rst.txt)


---

## 🔹 133. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.glom.html

# pyspark.RDD.glom#

RDD.glom()[[source]](../../_modules/pyspark/core/rdd.html#RDD.glom)#
    

Return an RDD created by coalescing all elements within each partition into a list.

New in version 0.7.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") coalescing all elements within each partition into a list

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 2)
    >>> sorted(rdd.glom().collect())
    [[1, 2], [3, 4]]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.glom.rst.txt)


---

## 🔹 134. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.groupBy.html

# pyspark.RDD.groupBy#

RDD.groupBy(_f_ , _numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.groupBy)#
    

Return an RDD of grouped items.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to compute the key

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

a function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") of grouped items

See also

[`RDD.groupByKey()`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")
    
[`pyspark.sql.DataFrame.groupBy()`](../pyspark.sql/api/pyspark.sql.DataFrame.groupBy.html#pyspark.sql.DataFrame.groupBy "pyspark.sql.DataFrame.groupBy")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 1, 2, 3, 5, 8])
    >>> result = rdd.groupBy(lambda x: x % 2).collect()
    >>> sorted([(x, sorted(y)) for (x, y) in result])
    [(0, [2, 8]), (1, [1, 1, 3, 5])]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.groupBy.rst.txt)


---

## 🔹 135. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.groupByKey.html

# pyspark.RDD.groupByKey#

RDD.groupByKey(_numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.groupByKey)#
    

Group the values for each key in the RDD into a single sequence. Hash-partitions the resulting RDD with numPartitions partitions.

New in version 0.7.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the grouped result for each key

See also

[`RDD.reduceByKey()`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")
    
[`RDD.combineByKey()`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")
    
[`RDD.aggregateByKey()`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")
    
[`RDD.foldByKey()`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")
    

Notes

If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will provide much better performance.

Examples
    
    
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
    >>> sorted(rdd.groupByKey().mapValues(len).collect())
    [('a', 2), ('b', 1)]
    >>> sorted(rdd.groupByKey().mapValues(list).collect())
    [('a', [1, 1]), ('b', [1])]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.groupByKey.rst.txt)


---

## 🔹 136. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.groupWith.html

# pyspark.RDD.groupWith#

RDD.groupWith(_other_ , _* others_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.groupWith)#
    

Alias for cogroup but with support for multiple RDDs.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**others**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

other [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")s

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and cogrouped values

See also

[`RDD.cogroup()`](pyspark.RDD.cogroup.html#pyspark.RDD.cogroup "pyspark.RDD.cogroup")
    
[`RDD.join()`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 5), ("b", 6)])
    >>> rdd2 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd3 = sc.parallelize([("a", 2)])
    >>> rdd4 = sc.parallelize([("b", 42)])
    >>> [(x, tuple(map(list, y))) for x, y in
    ...     sorted(list(rdd1.groupWith(rdd2, rdd3, rdd4).collect()))]
    [('a', ([5], [1], [2], [])), ('b', ([6], [4], [], [42]))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.groupWith.rst.txt)


---

## 🔹 137. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.histogram.html

# pyspark.RDD.histogram#

RDD.histogram(_buckets_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.histogram)#
    

Compute a histogram using the provided buckets. The buckets are all open to the right except for the last which is closed. e.g. [1,10,20,50] means the buckets are [1,10) [10,20) [20,50], which means 1<=x<10, 10<=x<20, 20<=x<=50. And on the input of 1 and 50 we would have a histogram of 1,0,1.

If your histogram is evenly spaced (e.g. [0, 10, 20, 30]), this can be switched from an O(log n) insertion to O(1) per element (where n is the number of buckets).

Buckets must be sorted, not contain any duplicates, and have at least two elements.

If buckets is a number, it will generate buckets which are evenly spaced between the minimum and maximum of the RDD. For example, if the min value is 0 and the max is 100, given buckets as 2, the resulting buckets will be [0,50) [50,100]. buckets must be at least 1. An exception is raised if the RDD contains infinity. If the elements in the RDD do not vary (max == min), a single bucket will be used.

New in version 1.2.0.

Parameters
    

**buckets** int, or list, or tuple
    

if buckets is a number, it computes a histogram of the data using buckets number of buckets evenly, otherwise, buckets is the provided buckets to bin the data.

Returns
    

tuple
    

a tuple of buckets and histogram

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(51))
    >>> rdd.histogram(2)
    ([0, 25, 50], [25, 26])
    >>> rdd.histogram([0, 5, 25, 50])
    ([0, 5, 25, 50], [5, 20, 26])
    >>> rdd.histogram([0, 15, 30, 45, 60])  # evenly spaced buckets
    ([0, 15, 30, 45, 60], [15, 15, 15, 6])
    >>> rdd = sc.parallelize(["ab", "ac", "b", "bd", "ef"])
    >>> rdd.histogram(("a", "b", "c"))
    (('a', 'b', 'c'), [2, 2])
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.histogram.rst.txt)


---

## 🔹 138. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.id.html

# pyspark.RDD.id#

RDD.id()[[source]](../../_modules/pyspark/core/rdd.html#RDD.id)#
    

A unique ID for this RDD (within its SparkContext).

New in version 0.7.0.

Returns
    

int
    

The unique ID for this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.id()  
    3
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.id.rst.txt)


---

## 🔹 139. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.intersection.html

# pyspark.RDD.intersection#

RDD.intersection(_other_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.intersection)#
    

Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.

New in version 1.0.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

the intersection of this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") and another one

See also

[`pyspark.sql.DataFrame.intersect()`](../pyspark.sql/api/pyspark.sql.DataFrame.intersect.html#pyspark.sql.DataFrame.intersect "pyspark.sql.DataFrame.intersect")
    

Notes

This method performs a shuffle internally.

Examples
    
    
    >>> rdd1 = sc.parallelize([1, 10, 2, 3, 4, 5])
    >>> rdd2 = sc.parallelize([1, 6, 2, 3, 7, 8])
    >>> rdd1.intersection(rdd2).collect()
    [1, 2, 3]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.intersection.rst.txt)


---

## 🔹 140. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.isCheckpointed.html

# pyspark.RDD.isCheckpointed#

RDD.isCheckpointed()[[source]](../../_modules/pyspark/core/rdd.html#RDD.isCheckpointed)#
    

Return whether this RDD is checkpointed and materialized, either reliably or locally.

New in version 0.7.0.

Returns
    

bool
    

whether this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") is checkpointed and materialized, either reliably or locally

See also

[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`RDD.getCheckpointFile()`](pyspark.RDD.getCheckpointFile.html#pyspark.RDD.getCheckpointFile "pyspark.RDD.getCheckpointFile")
    
[`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir")
    
[`SparkContext.getCheckpointDir()`](pyspark.SparkContext.getCheckpointDir.html#pyspark.SparkContext.getCheckpointDir "pyspark.SparkContext.getCheckpointDir")
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.isCheckpointed.rst.txt)


---

## 🔹 141. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.isEmpty.html

# pyspark.RDD.isEmpty#

RDD.isEmpty()[[source]](../../_modules/pyspark/core/rdd.html#RDD.isEmpty)#
    

Returns true if and only if the RDD contains no elements at all.

New in version 1.3.0.

Returns
    

bool
    

whether the [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") is empty

See also

[`RDD.first()`](pyspark.RDD.first.html#pyspark.RDD.first "pyspark.RDD.first")
    
[`pyspark.sql.DataFrame.isEmpty()`](../pyspark.sql/api/pyspark.sql.DataFrame.isEmpty.html#pyspark.sql.DataFrame.isEmpty "pyspark.sql.DataFrame.isEmpty")
    

Notes

An RDD may be empty even when it has at least 1 partition.

Examples
    
    
    >>> sc.parallelize([]).isEmpty()
    True
    >>> sc.parallelize([1]).isEmpty()
    False
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.isEmpty.rst.txt)


---

## 🔹 142. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.isLocallyCheckpointed.html

# pyspark.RDD.isLocallyCheckpointed#

RDD.isLocallyCheckpointed()[[source]](../../_modules/pyspark/core/rdd.html#RDD.isLocallyCheckpointed)#
    

Return whether this RDD is marked for local checkpointing.

Exposed for testing.

New in version 2.2.0.

Returns
    

bool
    

whether this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") is marked for local checkpointing

See also

[`RDD.localCheckpoint()`](pyspark.RDD.localCheckpoint.html#pyspark.RDD.localCheckpoint "pyspark.RDD.localCheckpoint")
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.isLocallyCheckpointed.rst.txt)


---

## 🔹 143. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.join.html

# pyspark.RDD.join#

RDD.join(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.join)#
    

Return an RDD containing all pairs of elements with matching keys in self and other.

Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in self and (k, v2) is in other.

Performs a hash join across the cluster.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing all pairs of elements with matching keys

See also

[`RDD.leftOuterJoin()`](pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")
    
[`RDD.rightOuterJoin()`](pyspark.RDD.rightOuterJoin.html#pyspark.RDD.rightOuterJoin "pyspark.RDD.rightOuterJoin")
    
[`RDD.fullOuterJoin()`](pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")
    
[`RDD.cogroup()`](pyspark.RDD.cogroup.html#pyspark.RDD.cogroup "pyspark.RDD.cogroup")
    
[`RDD.groupWith()`](pyspark.RDD.groupWith.html#pyspark.RDD.groupWith "pyspark.RDD.groupWith")
    
[`pyspark.sql.DataFrame.join()`](../pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join "pyspark.sql.DataFrame.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd2 = sc.parallelize([("a", 2), ("a", 3)])
    >>> sorted(rdd1.join(rdd2).collect())
    [('a', (1, 2)), ('a', (1, 3))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.join.rst.txt)


---

## 🔹 144. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.keyBy.html

# pyspark.RDD.keyBy#

RDD.keyBy(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.keyBy)#
    

Creates tuples of the elements in this RDD by applying f.

New in version 0.9.1.

Parameters
    

**f** function
    

a function to compute the key

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with the elements from this that are not in other

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.keys()`](pyspark.RDD.keys.html#pyspark.RDD.keys "pyspark.RDD.keys")
    
[`RDD.values()`](pyspark.RDD.values.html#pyspark.RDD.values "pyspark.RDD.values")
    

Examples
    
    
    >>> rdd1 = sc.parallelize(range(0,3)).keyBy(lambda x: x*x)
    >>> rdd2 = sc.parallelize(zip(range(0,5), range(0,5)))
    >>> [(x, list(map(list, y))) for x, y in sorted(rdd1.cogroup(rdd2).collect())]
    [(0, [[0], [0]]), (1, [[1], [1]]), (2, [[], [2]]), (3, [[], [3]]), (4, [[2], [4]])]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.keyBy.rst.txt)


---

## 🔹 145. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.keys.html

# pyspark.RDD.keys#

RDD.keys()[[source]](../../_modules/pyspark/core/rdd.html#RDD.keys)#
    

Return an RDD with the keys of each tuple.

New in version 0.7.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") only containing the keys

See also

[`RDD.values()`](pyspark.RDD.values.html#pyspark.RDD.values "pyspark.RDD.values")
    

Examples
    
    
    >>> rdd = sc.parallelize([(1, 2), (3, 4)]).keys()
    >>> rdd.collect()
    [1, 3]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.keys.rst.txt)


---

## 🔹 146. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.leftOuterJoin.html

# pyspark.RDD.leftOuterJoin#

RDD.leftOuterJoin(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.leftOuterJoin)#
    

Perform a left outer join of self and other.

For each element (k, v) in self, the resulting RDD will either contain all pairs (k, (v, w)) for w in other, or the pair (k, (v, None)) if no elements in other have key k.

Hash-partitions the resulting RDD into the given number of partitions.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing all pairs of elements with matching keys

See also

[`RDD.join()`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")
    
[`RDD.rightOuterJoin()`](pyspark.RDD.rightOuterJoin.html#pyspark.RDD.rightOuterJoin "pyspark.RDD.rightOuterJoin")
    
[`RDD.fullOuterJoin()`](pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")
    
[`pyspark.sql.DataFrame.join()`](../pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join "pyspark.sql.DataFrame.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd2 = sc.parallelize([("a", 2)])
    >>> sorted(rdd1.leftOuterJoin(rdd2).collect())
    [('a', (1, 2)), ('b', (4, None))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.leftOuterJoin.rst.txt)


---

## 🔹 147. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.localCheckpoint.html

# pyspark.RDD.localCheckpoint#

RDD.localCheckpoint()[[source]](../../_modules/pyspark/core/rdd.html#RDD.localCheckpoint)#
    

Mark this RDD for local checkpointing using Sparkâs existing caching layer.

This method is for users who wish to truncate RDD lineages while skipping the expensive step of replicating the materialized data in a reliable distributed file system. This is useful for RDDs with long lineages that need to be truncated periodically (e.g. GraphX).

Local checkpointing sacrifices fault-tolerance for performance. In particular, checkpointed data is written to ephemeral local storage in the executors instead of to a reliable, fault-tolerant storage. The effect is that if an executor fails during the computation, the checkpointed data may no longer be accessible, causing an irrecoverable job failure.

This is NOT safe to use with dynamic allocation, which removes executors along with their cached blocks. If you must use both features, you are advised to set spark.dynamicAllocation.cachedExecutorIdleTimeout to a high value.

The checkpoint directory set through [`SparkContext.setCheckpointDir()`](pyspark.SparkContext.setCheckpointDir.html#pyspark.SparkContext.setCheckpointDir "pyspark.SparkContext.setCheckpointDir") is not used.

New in version 2.2.0.

See also

[`RDD.checkpoint()`](pyspark.RDD.checkpoint.html#pyspark.RDD.checkpoint "pyspark.RDD.checkpoint")
    
[`RDD.isLocallyCheckpointed()`](pyspark.RDD.isLocallyCheckpointed.html#pyspark.RDD.isLocallyCheckpointed "pyspark.RDD.isLocallyCheckpointed")
    

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.isLocallyCheckpointed()
    False
    
    
    
    >>> rdd.localCheckpoint()
    >>> rdd.isLocallyCheckpointed()
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.localCheckpoint.rst.txt)


---

## 🔹 148. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.lookup.html

# pyspark.RDD.lookup#

RDD.lookup(_key_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.lookup)#
    

Return the list of values in the RDD for key key. This operation is done efficiently if the RDD has a known partitioner by only searching the partition that the key maps to.

New in version 1.2.0.

Parameters
    

**key** K
    

the key to look up

Returns
    

list
    

the list of values in the [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") for key key

Examples
    
    
    >>> l = range(1000)
    >>> rdd = sc.parallelize(zip(l, l), 10)
    >>> rdd.lookup(42)  # slow
    [42]
    >>> sorted = rdd.sortByKey()
    >>> sorted.lookup(42)  # fast
    [42]
    >>> sorted.lookup(1024)
    []
    >>> rdd2 = sc.parallelize([(('a', 'b'), 'c')]).groupByKey()
    >>> list(rdd2.lookup(('a', 'b'))[0])
    ['c']
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.lookup.rst.txt)


---

## 🔹 149. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.map.html

# pyspark.RDD.map#

RDD.map(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.map)#
    

Return a new RDD by applying a function to each element of this RDD.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to run on each element of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to all elements

See also

[`RDD.flatMap()`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")
    
[`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")
    
[`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")
    
[`RDD.mapPartitionsWithSplit()`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")
    

Examples
    
    
    >>> rdd = sc.parallelize(["b", "a", "c"])
    >>> sorted(rdd.map(lambda x: (x, 1)).collect())
    [('a', 1), ('b', 1), ('c', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.map.rst.txt)


---

## 🔹 150. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.mapPartitions.html

# pyspark.RDD.mapPartitions#

RDD.mapPartitions(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.mapPartitions)#
    

Return a new RDD by applying a function to each partition of this RDD.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to run on each partition of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each partition

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.flatMap()`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")
    
[`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")
    
[`RDD.mapPartitionsWithSplit()`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")
    
[`RDDBarrier.mapPartitions()`](pyspark.RDDBarrier.mapPartitions.html#pyspark.RDDBarrier.mapPartitions "pyspark.RDDBarrier.mapPartitions")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 2)
    >>> def f(iterator): yield sum(iterator)
    ...
    >>> rdd.mapPartitions(f).collect()
    [3, 7]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.mapPartitions.rst.txt)


---

## 🔹 151. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.mapPartitionsWithIndex.html

# pyspark.RDD.mapPartitionsWithIndex#

RDD.mapPartitionsWithIndex(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.mapPartitionsWithIndex)#
    

Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to run on each partition of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each partition

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.flatMap()`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")
    
[`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")
    
[`RDD.mapPartitionsWithSplit()`](pyspark.RDD.mapPartitionsWithSplit.html#pyspark.RDD.mapPartitionsWithSplit "pyspark.RDD.mapPartitionsWithSplit")
    
[`RDDBarrier.mapPartitionsWithIndex()`](pyspark.RDDBarrier.mapPartitionsWithIndex.html#pyspark.RDDBarrier.mapPartitionsWithIndex "pyspark.RDDBarrier.mapPartitionsWithIndex")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 4)
    >>> def f(splitIndex, iterator): yield splitIndex
    ...
    >>> rdd.mapPartitionsWithIndex(f).sum()
    6
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.mapPartitionsWithIndex.rst.txt)


---

## 🔹 152. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.mapPartitionsWithSplit.html

# pyspark.RDD.mapPartitionsWithSplit#

RDD.mapPartitionsWithSplit(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.mapPartitionsWithSplit)#
    

Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.

New in version 0.7.0.

Deprecated since version 0.9.0: use meth:RDD.mapPartitionsWithIndex instead.

Parameters
    

**f** function
    

a function to run on each partition of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each partition

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.flatMap()`](pyspark.RDD.flatMap.html#pyspark.RDD.flatMap "pyspark.RDD.flatMap")
    
[`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")
    
[`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 4)
    >>> def f(splitIndex, iterator): yield splitIndex
    ...
    >>> rdd.mapPartitionsWithSplit(f).sum()
    6
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.mapPartitionsWithSplit.rst.txt)


---

## 🔹 153. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.mapValues.html

# pyspark.RDD.mapValues#

RDD.mapValues(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.mapValues)#
    

Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDDâs partitioning.

New in version 0.7.0.

Parameters
    

**f** function
    

a function to turn a V into a U

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the mapped value

See also

[`RDD.map()`](pyspark.RDD.map.html#pyspark.RDD.map "pyspark.RDD.map")
    
[`RDD.flatMapValues()`](pyspark.RDD.flatMapValues.html#pyspark.RDD.flatMapValues "pyspark.RDD.flatMapValues")
    

Examples
    
    
    >>> rdd = sc.parallelize([("a", ["apple", "banana", "lemon"]), ("b", ["grapes"])])
    >>> def f(x): return len(x)
    ...
    >>> rdd.mapValues(f).collect()
    [('a', 3), ('b', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.mapValues.rst.txt)


---

## 🔹 154. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.max.html

# pyspark.RDD.max#

RDD.max(_key =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.max)#
    

Find the maximum item in this RDD.

New in version 1.0.0.

Parameters
    

**key** function, optional
    

A function used to generate key for comparing

Returns
    

T
    

the maximum item

See also

[`RDD.min()`](pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")
    

Examples
    
    
    >>> rdd = sc.parallelize([1.0, 5.0, 43.0, 10.0])
    >>> rdd.max()
    43.0
    >>> rdd.max(key=str)
    5.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.max.rst.txt)


---

## 🔹 155. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.mean.html

# pyspark.RDD.mean#

RDD.mean()[[source]](../../_modules/pyspark/core/rdd.html#RDD.mean)#
    

Compute the mean of this RDDâs elements.

New in version 0.9.1.

Returns
    

float
    

the mean of all elements

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    
[`RDD.sum()`](pyspark.RDD.sum.html#pyspark.RDD.sum "pyspark.RDD.sum")
    
[`RDD.meanApprox()`](pyspark.RDD.meanApprox.html#pyspark.RDD.meanApprox "pyspark.RDD.meanApprox")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3]).mean()
    2.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.mean.rst.txt)


---

## 🔹 156. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.meanApprox.html

# pyspark.RDD.meanApprox#

RDD.meanApprox(_timeout_ , _confidence =0.95_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.meanApprox)#
    

Approximate operation to return the mean within a timeout or meet the confidence.

New in version 1.2.0.

Parameters
    

**timeout** int
    

maximum time to wait for the job, in milliseconds

**confidence** float
    

the desired statistical confidence in the result

Returns
    

`BoundedFloat`
    

a potentially incomplete result, with error bounds

See also

[`RDD.mean()`](pyspark.RDD.mean.html#pyspark.RDD.mean "pyspark.RDD.mean")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(1000), 10)
    >>> r = sum(range(1000)) / 1000.0
    >>> abs(rdd.meanApprox(1000) - r) / r < 0.05
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.meanApprox.rst.txt)


---

## 🔹 157. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.min.html

# pyspark.RDD.min#

RDD.min(_key =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.min)#
    

Find the minimum item in this RDD.

New in version 1.0.0.

Parameters
    

**key** function, optional
    

A function used to generate key for comparing

Returns
    

T
    

the minimum item

See also

[`RDD.max()`](pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")
    

Examples
    
    
    >>> rdd = sc.parallelize([2.0, 5.0, 43.0, 10.0])
    >>> rdd.min()
    2.0
    >>> rdd.min(key=str)
    10.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.min.rst.txt)


---

## 🔹 158. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.name.html

# pyspark.RDD.name#

RDD.name()[[source]](../../_modules/pyspark/core/rdd.html#RDD.name)#
    

Return the name of this RDD.

New in version 1.0.0.

Returns
    

str
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") name

See also

[`RDD.setName()`](pyspark.RDD.setName.html#pyspark.RDD.setName "pyspark.RDD.setName")
    

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.name() == None
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.name.rst.txt)


---

## 🔹 159. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.partitionBy.html

# pyspark.RDD.partitionBy#

RDD.partitionBy(_numPartitions_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.partitionBy)#
    

Return a copy of the RDD partitioned using the specified partitioner.

New in version 0.7.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") partitioned using the specified partitioner

See also

[`RDD.repartition()`](pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")
    
[`RDD.repartitionAndSortWithinPartitions()`](pyspark.RDD.repartitionAndSortWithinPartitions.html#pyspark.RDD.repartitionAndSortWithinPartitions "pyspark.RDD.repartitionAndSortWithinPartitions")
    

Examples
    
    
    >>> pairs = sc.parallelize([1, 2, 3, 4, 2, 4, 1]).map(lambda x: (x, x))
    >>> sets = pairs.partitionBy(2).glom().collect()
    >>> len(set(sets[0]).intersection(set(sets[1])))
    0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.partitionBy.rst.txt)


---

## 🔹 160. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.persist.html

# pyspark.RDD.persist#

RDD.persist(_storageLevel =StorageLevel(False, True, False, False, 1)_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.persist)#
    

Set this RDDâs storage level to persist its values across operations after the first time it is computed. This can only be used to assign a new storage level if the RDD does not have a storage level set yet. If no storage level is specified defaults to (MEMORY_ONLY).

New in version 0.9.1.

Parameters
    

**storageLevel**[` StorageLevel`](pyspark.StorageLevel.html#pyspark.StorageLevel "pyspark.StorageLevel"), default MEMORY_ONLY
    

the target storage level

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

The same [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with storage level set to storageLevel.

See also

[`RDD.cache()`](pyspark.RDD.cache.html#pyspark.RDD.cache "pyspark.RDD.cache")
    
[`RDD.unpersist()`](pyspark.RDD.unpersist.html#pyspark.RDD.unpersist "pyspark.RDD.unpersist")
    
[`RDD.getStorageLevel()`](pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")
    

Examples
    
    
    >>> rdd = sc.parallelize(["b", "a", "c"])
    >>> rdd.persist().is_cached
    True
    >>> str(rdd.getStorageLevel())
    'Memory Serialized 1x Replicated'
    >>> _ = rdd.unpersist()
    >>> rdd.is_cached
    False
    
    
    
    >>> from pyspark import StorageLevel
    >>> rdd2 = sc.range(5)
    >>> _ = rdd2.persist(StorageLevel.MEMORY_AND_DISK)
    >>> rdd2.is_cached
    True
    >>> str(rdd2.getStorageLevel())
    'Disk Memory Serialized 1x Replicated'
    

Can not override existing storage level
    
    
    >>> _ = rdd2.persist(StorageLevel.MEMORY_ONLY_2)
    Traceback (most recent call last):
        ...
    py4j.protocol.Py4JJavaError: ...
    

Assign another storage level after unpersist
    
    
    >>> _ = rdd2.unpersist()
    >>> rdd2.is_cached
    False
    >>> _ = rdd2.persist(StorageLevel.MEMORY_ONLY_2)
    >>> str(rdd2.getStorageLevel())
    'Memory Serialized 2x Replicated'
    >>> rdd2.is_cached
    True
    >>> _ = rdd2.unpersist()
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.persist.rst.txt)


---

## 🔹 161. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.pipe.html

# pyspark.RDD.pipe#

RDD.pipe(_command_ , _env =None_, _checkCode =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.pipe)#
    

Return an RDD created by piping elements to a forked external process.

New in version 0.7.0.

Parameters
    

**command** str
    

command to run.

**env** dict, optional
    

environment variables to set.

**checkCode** bool, optional
    

whether to check the return value of the shell command.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") of strings

Examples
    
    
    >>> sc.parallelize(['1', '2', '', '3']).pipe('cat').collect()
    ['1', '2', '', '3']
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.pipe.rst.txt)


---

## 🔹 162. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.randomSplit.html

# pyspark.RDD.randomSplit#

RDD.randomSplit(_weights_ , _seed =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.randomSplit)#
    

Randomly splits this RDD with the provided weights.

New in version 1.3.0.

Parameters
    

**weights** list
    

weights for splits, will be normalized if they donât sum to 1

**seed** int, optional
    

random seed

Returns
    

list
    

split [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")s in a list

See also

[`pyspark.sql.DataFrame.randomSplit()`](../pyspark.sql/api/pyspark.sql.DataFrame.randomSplit.html#pyspark.sql.DataFrame.randomSplit "pyspark.sql.DataFrame.randomSplit")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(500), 1)
    >>> rdd1, rdd2 = rdd.randomSplit([2, 3], 17)
    >>> len(rdd1.collect() + rdd2.collect())
    500
    >>> 150 < rdd1.count() < 250
    True
    >>> 250 < rdd2.count() < 350
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.randomSplit.rst.txt)


---

## 🔹 163. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.reduce.html

# pyspark.RDD.reduce#

RDD.reduce(_f_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.reduce)#
    

Reduces the elements of this RDD using the specified commutative and associative binary operator. Currently reduces partitions locally.

New in version 0.7.0.

Parameters
    

**f** function
    

the reduce function

Returns
    

T
    

the aggregated result

See also

[`RDD.treeReduce()`](pyspark.RDD.treeReduce.html#pyspark.RDD.treeReduce "pyspark.RDD.treeReduce")
    
[`RDD.aggregate()`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")
    
[`RDD.treeAggregate()`](pyspark.RDD.treeAggregate.html#pyspark.RDD.treeAggregate "pyspark.RDD.treeAggregate")
    

Examples
    
    
    >>> from operator import add
    >>> sc.parallelize([1, 2, 3, 4, 5]).reduce(add)
    15
    >>> sc.parallelize((2 for _ in range(10))).map(lambda x: 1).cache().reduce(add)
    10
    >>> sc.parallelize([]).reduce(add)
    Traceback (most recent call last):
        ...
    ValueError: Can not reduce() empty RDD
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.reduce.rst.txt)


---

## 🔹 164. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.reduceByKey.html

# pyspark.RDD.reduceByKey#

RDD.reduceByKey(_func_ , _numPartitions=None_ , _partitionFunc= <function portable_hash>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.reduceByKey)#
    

Merge the values for each key using an associative and commutative reduce function.

This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a âcombinerâ in MapReduce.

Output will be partitioned with numPartitions partitions, or the default parallelism level if numPartitions is not specified. Default partitioner is hash-partition.

New in version 1.6.0.

Parameters
    

**func** function
    

the reduce function

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

function to compute the partition index

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the keys and the aggregated result for each key

See also

[`RDD.reduceByKeyLocally()`](pyspark.RDD.reduceByKeyLocally.html#pyspark.RDD.reduceByKeyLocally "pyspark.RDD.reduceByKeyLocally")
    
[`RDD.combineByKey()`](pyspark.RDD.combineByKey.html#pyspark.RDD.combineByKey "pyspark.RDD.combineByKey")
    
[`RDD.aggregateByKey()`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")
    
[`RDD.foldByKey()`](pyspark.RDD.foldByKey.html#pyspark.RDD.foldByKey "pyspark.RDD.foldByKey")
    
[`RDD.groupByKey()`](pyspark.RDD.groupByKey.html#pyspark.RDD.groupByKey "pyspark.RDD.groupByKey")
    

Examples
    
    
    >>> from operator import add
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
    >>> sorted(rdd.reduceByKey(add).collect())
    [('a', 2), ('b', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.reduceByKey.rst.txt)


---

## 🔹 165. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.reduceByKeyLocally.html

# pyspark.RDD.reduceByKeyLocally#

RDD.reduceByKeyLocally(_func_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.reduceByKeyLocally)#
    

Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a dictionary.

This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a âcombinerâ in MapReduce.

New in version 0.7.0.

Parameters
    

**func** function
    

the reduce function

Returns
    

dict
    

a dict containing the keys and the aggregated result for each key

See also

[`RDD.reduceByKey()`](pyspark.RDD.reduceByKey.html#pyspark.RDD.reduceByKey "pyspark.RDD.reduceByKey")
    
[`RDD.aggregateByKey()`](pyspark.RDD.aggregateByKey.html#pyspark.RDD.aggregateByKey "pyspark.RDD.aggregateByKey")
    

Examples
    
    
    >>> from operator import add
    >>> rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
    >>> sorted(rdd.reduceByKeyLocally(add).items())
    [('a', 2), ('b', 1)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.reduceByKeyLocally.rst.txt)


---

## 🔹 166. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.repartition.html

# pyspark.RDD.repartition#

RDD.repartition(_numPartitions_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.repartition)#
    

> Return a new RDD that has exactly numPartitions partitions.
> 
> Can increase or decrease the level of parallelism in this RDD. Internally, this uses a shuffle to redistribute data. If you are decreasing the number of partitions in this RDD, consider using coalesce, which can avoid performing a shuffle.

New in version 1.0.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with exactly numPartitions partitions

See also

[`RDD.coalesce()`](pyspark.RDD.coalesce.html#pyspark.RDD.coalesce "pyspark.RDD.coalesce")
    
[`RDD.partitionBy()`](pyspark.RDD.partitionBy.html#pyspark.RDD.partitionBy "pyspark.RDD.partitionBy")
    
[`RDD.repartitionAndSortWithinPartitions()`](pyspark.RDD.repartitionAndSortWithinPartitions.html#pyspark.RDD.repartitionAndSortWithinPartitions "pyspark.RDD.repartitionAndSortWithinPartitions")
    

Examples
    
    
    >>> rdd = sc.parallelize([1,2,3,4,5,6,7], 4)
    >>> sorted(rdd.glom().collect())
    [[1], [2, 3], [4, 5], [6, 7]]
    >>> len(rdd.repartition(2).glom().collect())
    2
    >>> len(rdd.repartition(10).glom().collect())
    10
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.repartition.rst.txt)


---

## 🔹 167. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.repartitionAndSortWithinPartitions.html

# pyspark.RDD.repartitionAndSortWithinPartitions#

RDD.repartitionAndSortWithinPartitions(_numPartitions=None_ , _partitionFunc= <function portable_hash>_, _ascending=True_ , _keyfunc= <function RDD.<lambda>>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.repartitionAndSortWithinPartitions)#
    

Repartition the RDD according to the given partitioner and, within each resulting partition, sort records by their keys.

New in version 1.2.0.

Parameters
    

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**partitionFunc** function, optional, default portable_hash
    

a function to compute the partition index

**ascending** bool, optional, default True
    

sort the keys in ascending or descending order

**keyfunc** function, optional, default identity mapping
    

a function to compute the key

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

See also

[`RDD.repartition()`](pyspark.RDD.repartition.html#pyspark.RDD.repartition "pyspark.RDD.repartition")
    
[`RDD.partitionBy()`](pyspark.RDD.partitionBy.html#pyspark.RDD.partitionBy "pyspark.RDD.partitionBy")
    
[`RDD.sortBy()`](pyspark.RDD.sortBy.html#pyspark.RDD.sortBy "pyspark.RDD.sortBy")
    
[`RDD.sortByKey()`](pyspark.RDD.sortByKey.html#pyspark.RDD.sortByKey "pyspark.RDD.sortByKey")
    

Examples
    
    
    >>> rdd = sc.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
    >>> rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, True)
    >>> rdd2.glom().collect()
    [[(0, 5), (0, 8), (2, 6)], [(1, 3), (3, 8), (3, 8)]]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.repartitionAndSortWithinPartitions.rst.txt)


---

## 🔹 168. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.rightOuterJoin.html

# pyspark.RDD.rightOuterJoin#

RDD.rightOuterJoin(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.rightOuterJoin)#
    

Perform a right outer join of self and other.

For each element (k, w) in other, the resulting RDD will either contain all pairs (k, (v, w)) for v in this, or the pair (k, (None, w)) if no elements in self have key k.

Hash-partitions the resulting RDD into the given number of partitions.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing all pairs of elements with matching keys

See also

[`RDD.join()`](pyspark.RDD.join.html#pyspark.RDD.join "pyspark.RDD.join")
    
[`RDD.leftOuterJoin()`](pyspark.RDD.leftOuterJoin.html#pyspark.RDD.leftOuterJoin "pyspark.RDD.leftOuterJoin")
    
[`RDD.fullOuterJoin()`](pyspark.RDD.fullOuterJoin.html#pyspark.RDD.fullOuterJoin "pyspark.RDD.fullOuterJoin")
    
[`pyspark.sql.DataFrame.join()`](../pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join "pyspark.sql.DataFrame.join")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4)])
    >>> rdd2 = sc.parallelize([("a", 2)])
    >>> sorted(rdd2.rightOuterJoin(rdd1).collect())
    [('a', (2, 1)), ('b', (None, 4))]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.rightOuterJoin.rst.txt)


---

## 🔹 169. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sample.html

# pyspark.RDD.sample#

RDD.sample(_withReplacement_ , _fraction_ , _seed =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.sample)#
    

Return a sampled subset of this RDD.

New in version 0.7.0.

Parameters
    

**withReplacement** bool
    

can elements be sampled multiple times (replaced when sampled out)

**fraction** float
    

expected size of the sample as a fraction of this RDDâs size without replacement: probability that each element is chosen; fraction must be [0, 1] with replacement: expected number of times each element is chosen; fraction must be >= 0

**seed** int, optional
    

seed for the random number generator

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing a sampled subset of elements

See also

[`RDD.takeSample()`](pyspark.RDD.takeSample.html#pyspark.RDD.takeSample "pyspark.RDD.takeSample")
    
[`RDD.sampleByKey()`](pyspark.RDD.sampleByKey.html#pyspark.RDD.sampleByKey "pyspark.RDD.sampleByKey")
    
[`pyspark.sql.DataFrame.sample()`](../pyspark.sql/api/pyspark.sql.DataFrame.sample.html#pyspark.sql.DataFrame.sample "pyspark.sql.DataFrame.sample")
    

Notes

This is not guaranteed to provide exactly the fraction specified of the total count of the given `DataFrame`.

Examples
    
    
    >>> rdd = sc.parallelize(range(100), 4)
    >>> 6 <= rdd.sample(False, 0.1, 81).count() <= 14
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sample.rst.txt)


---

## 🔹 170. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sampleByKey.html

# pyspark.RDD.sampleByKey#

RDD.sampleByKey(_withReplacement_ , _fractions_ , _seed =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.sampleByKey)#
    

Return a subset of this RDD sampled by key (via stratified sampling). Create a sample of this RDD using variable sampling rates for different keys as specified by fractions, a key to sampling rate map.

New in version 0.7.0.

Parameters
    

**withReplacement** bool
    

whether to sample with or without replacement

**fractions** dict
    

map of specific keys to sampling rates

**seed** int, optional
    

seed for the random number generator

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the stratified sampling result

See also

[`RDD.sample()`](pyspark.RDD.sample.html#pyspark.RDD.sample "pyspark.RDD.sample")
    

Examples
    
    
    >>> fractions = {"a": 0.2, "b": 0.1}
    >>> rdd = sc.parallelize(fractions.keys()).cartesian(sc.parallelize(range(0, 1000)))
    >>> sample = dict(rdd.sampleByKey(False, fractions, 2).groupByKey().collect())
    >>> 100 < len(sample["a"]) < 300 and 50 < len(sample["b"]) < 150
    True
    >>> max(sample["a"]) <= 999 and min(sample["a"]) >= 0
    True
    >>> max(sample["b"]) <= 999 and min(sample["b"]) >= 0
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sampleByKey.rst.txt)


---

## 🔹 171. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sampleStdev.html

# pyspark.RDD.sampleStdev#

RDD.sampleStdev()[[source]](../../_modules/pyspark/core/rdd.html#RDD.sampleStdev)#
    

Compute the sample standard deviation of this RDDâs elements (which corrects for bias in estimating the standard deviation by dividing by N-1 instead of N).

New in version 0.9.1.

Returns
    

float
    

the sample standard deviation of all elements

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    
[`RDD.stdev()`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")
    
[`RDD.variance()`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")
    
[`RDD.sampleVariance()`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3]).sampleStdev()
    1.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sampleStdev.rst.txt)


---

## 🔹 172. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sampleVariance.html

# pyspark.RDD.sampleVariance#

RDD.sampleVariance()[[source]](../../_modules/pyspark/core/rdd.html#RDD.sampleVariance)#
    

Compute the sample variance of this RDDâs elements (which corrects for bias in estimating the variance by dividing by N-1 instead of N).

New in version 0.9.1.

Returns
    

float
    

the sample variance of all elements

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    
[`RDD.variance()`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")
    
[`RDD.stdev()`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")
    
[`RDD.sampleStdev()`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3]).sampleVariance()
    1.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sampleVariance.rst.txt)


---

## 🔹 173. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsHadoopDataset.html

# pyspark.RDD.saveAsHadoopDataset#

RDD.saveAsHadoopDataset(_conf_ , _keyConverter =None_, _valueConverter =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsHadoopDataset)#
    

Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package). Keys/values are converted for output using either user specified converters or, by default, âorg.apache.spark.api.python.JavaToWritableConverterâ.

New in version 1.1.0.

Parameters
    

**conf** dict
    

Hadoop job configuration

**keyConverter** str, optional
    

fully qualified classname of key converter (None by default)

**valueConverter** str, optional
    

fully qualified classname of value converter (None by default)

See also

[`SparkContext.hadoopRDD()`](pyspark.SparkContext.hadoopRDD.html#pyspark.SparkContext.hadoopRDD "pyspark.SparkContext.hadoopRDD")
    
[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsHadoopDataset") as d:
    ...     path = os.path.join(d, "old_hadoop_file")
    ...
    ...     # Create the conf for writing
    ...     write_conf = {
    ...         "mapred.output.format.class": output_format_class,
    ...         "mapreduce.job.output.key.class": key_class,
    ...         "mapreduce.job.output.value.class": value_class,
    ...         "mapreduce.output.fileoutputformat.outputdir": path,
    ...     }
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsHadoopDataset(conf=write_conf)
    ...
    ...     # Create the conf for reading
    ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
    ...
    ...     # Load this Hadoop file as an RDD
    ...     loaded = sc.hadoopRDD(input_format_class, key_class, value_class, conf=read_conf)
    ...     sorted(loaded.collect())
    [(0, '1\t'), (0, '1\ta'), (0, '3\tx')]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsHadoopDataset.rst.txt)


---

## 🔹 174. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsHadoopFile.html

# pyspark.RDD.saveAsHadoopFile#

RDD.saveAsHadoopFile(_path_ , _outputFormatClass_ , _keyClass =None_, _valueClass =None_, _keyConverter =None_, _valueConverter =None_, _conf =None_, _compressionCodecClass =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsHadoopFile)#
    

Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the old Hadoop OutputFormat API (mapred package). Key and value types will be inferred if not specified. Keys and values are converted for output using either user specified converters or âorg.apache.spark.api.python.JavaToWritableConverterâ. The conf is applied on top of the base Hadoop conf associated with the SparkContext of this RDD to create a merged Hadoop MapReduce job configuration for saving the data.

New in version 1.1.0.

Parameters
    

**path** str
    

path to Hadoop file

**outputFormatClass** str
    

fully qualified classname of Hadoop OutputFormat (e.g. âorg.apache.hadoop.mapred.SequenceFileOutputFormatâ)

**keyClass** str, optional
    

fully qualified classname of key Writable class (e.g. âorg.apache.hadoop.io.IntWritableâ, None by default)

**valueClass** str, optional
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.Textâ, None by default)

**keyConverter** str, optional
    

fully qualified classname of key converter (None by default)

**valueConverter** str, optional
    

fully qualified classname of value converter (None by default)

**conf** dict, optional
    

(None by default)

**compressionCodecClass** str
    

fully qualified classname of the compression codec class i.e. âorg.apache.hadoop.io.compress.GzipCodecâ (None by default)

See also

[`SparkContext.hadoopFile()`](pyspark.SparkContext.hadoopFile.html#pyspark.SparkContext.hadoopFile "pyspark.SparkContext.hadoopFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapred.TextOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapred.TextInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsHadoopFile") as d:
    ...     path = os.path.join(d, "old_hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsHadoopFile(path, output_format_class, key_class, value_class)
    ...
    ...     # Load this Hadoop file as an RDD
    ...     loaded = sc.hadoopFile(path, input_format_class, key_class, value_class)
    ...     sorted(loaded.collect())
    [(0, '1\t'), (0, '1\ta'), (0, '3\tx')]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsHadoopFile.rst.txt)


---

## 🔹 175. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsNewAPIHadoopDataset.html

# pyspark.RDD.saveAsNewAPIHadoopDataset#

RDD.saveAsNewAPIHadoopDataset(_conf_ , _keyConverter =None_, _valueConverter =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsNewAPIHadoopDataset)#
    

Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package). Keys/values are converted for output using either user specified converters or, by default, âorg.apache.spark.api.python.JavaToWritableConverterâ.

New in version 1.1.0.

Parameters
    

**conf** dict
    

Hadoop job configuration

**keyConverter** str, optional
    

fully qualified classname of key converter (None by default)

**valueConverter** str, optional
    

fully qualified classname of value converter (None by default)

See also

[`SparkContext.newAPIHadoopRDD()`](pyspark.SparkContext.newAPIHadoopRDD.html#pyspark.SparkContext.newAPIHadoopRDD "pyspark.SparkContext.newAPIHadoopRDD")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    >>> input_format_class = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
    >>> key_class = "org.apache.hadoop.io.IntWritable"
    >>> value_class = "org.apache.hadoop.io.Text"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsNewAPIHadoopDataset") as d:
    ...     path = os.path.join(d, "new_hadoop_file")
    ...
    ...     # Create the conf for writing
    ...     write_conf = {
    ...         "mapreduce.job.outputformat.class": (output_format_class),
    ...         "mapreduce.job.output.key.class": key_class,
    ...         "mapreduce.job.output.value.class": value_class,
    ...         "mapreduce.output.fileoutputformat.outputdir": path,
    ...     }
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsNewAPIHadoopDataset(conf=write_conf)
    ...
    ...     # Create the conf for reading
    ...     read_conf = {"mapreduce.input.fileinputformat.inputdir": path}
    ...
    ...     # Load this Hadoop file as an RDD
    ...     loaded = sc.newAPIHadoopRDD(input_format_class,
    ...         key_class, value_class, conf=read_conf)
    ...     sorted(loaded.collect())
    [(1, ''), (1, 'a'), (3, 'x')]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsNewAPIHadoopDataset.rst.txt)


---

## 🔹 176. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsNewAPIHadoopFile.html

# pyspark.RDD.saveAsNewAPIHadoopFile#

RDD.saveAsNewAPIHadoopFile(_path_ , _outputFormatClass_ , _keyClass =None_, _valueClass =None_, _keyConverter =None_, _valueConverter =None_, _conf =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsNewAPIHadoopFile)#
    

Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the new Hadoop OutputFormat API (mapreduce package). Key and value types will be inferred if not specified. Keys and values are converted for output using either user specified converters or âorg.apache.spark.api.python.JavaToWritableConverterâ. The conf is applied on top of the base Hadoop conf associated with the SparkContext of this RDD to create a merged Hadoop MapReduce job configuration for saving the data.

New in version 1.1.0.

Parameters
    

**path** str
    

path to Hadoop file

**outputFormatClass** str
    

fully qualified classname of Hadoop OutputFormat (e.g. âorg.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormatâ)

**keyClass** str, optional
    

fully qualified classname of key Writable class
    

(e.g. âorg.apache.hadoop.io.IntWritableâ, None by default)

**valueClass** str, optional
    

fully qualified classname of value Writable class (e.g. âorg.apache.hadoop.io.Textâ, None by default)

**keyConverter** str, optional
    

fully qualified classname of key converter (None by default)

**valueConverter** str, optional
    

fully qualified classname of value converter (None by default)

**conf** dict, optional
    

Hadoop job configuration (None by default)

See also

[`SparkContext.newAPIHadoopFile()`](pyspark.SparkContext.newAPIHadoopFile.html#pyspark.SparkContext.newAPIHadoopFile "pyspark.SparkContext.newAPIHadoopFile")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`RDD.saveAsSequenceFile()`](pyspark.RDD.saveAsSequenceFile.html#pyspark.RDD.saveAsSequenceFile "pyspark.RDD.saveAsSequenceFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the class of output format
    
    
    >>> output_format_class = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsNewAPIHadoopFile") as d:
    ...     path = os.path.join(d, "hadoop_file")
    ...
    ...     # Write a temporary Hadoop file
    ...     rdd = sc.parallelize([(1, {3.0: "bb"}), (2, {1.0: "aa"}), (3, {2.0: "dd"})])
    ...     rdd.saveAsNewAPIHadoopFile(path, output_format_class)
    ...
    ...     # Load this Hadoop file as an RDD
    ...     sorted(sc.sequenceFile(path).collect())
    [(1, {3.0: 'bb'}), (2, {1.0: 'aa'}), (3, {2.0: 'dd'})]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsNewAPIHadoopFile.rst.txt)


---

## 🔹 177. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsPickleFile.html

# pyspark.RDD.saveAsPickleFile#

RDD.saveAsPickleFile(_path_ , _batchSize =10_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsPickleFile)#
    

Save this RDD as a SequenceFile of serialized objects. The serializer used is `pyspark.serializers.CPickleSerializer`, default batch size is 10.

New in version 1.1.0.

Parameters
    

**path** str
    

path to pickled file

**batchSize** int, optional, default 10
    

the number of Python objects represented as a single Java object.

See also

[`SparkContext.pickleFile()`](pyspark.SparkContext.pickleFile.html#pyspark.SparkContext.pickleFile "pyspark.SparkContext.pickleFile")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory(prefix="saveAsPickleFile") as d:
    ...     path = os.path.join(d, "pickle_file")
    ...
    ...     # Write a temporary pickled file
    ...     sc.parallelize(range(10)).saveAsPickleFile(path, 3)
    ...
    ...     # Load picked file as an RDD
    ...     sorted(sc.pickleFile(path, 3).collect())
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsPickleFile.rst.txt)


---

## 🔹 178. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsSequenceFile.html

# pyspark.RDD.saveAsSequenceFile#

RDD.saveAsSequenceFile(_path_ , _compressionCodecClass =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsSequenceFile)#
    

Output a Python RDD of key-value pairs (of form `RDD[(K, V)]`) to any Hadoop file system, using the âorg.apache.hadoop.io.Writableâ types that we convert from the RDDâs key and value types. The mechanism is as follows:

>   1. Pickle is used to convert pickled Python RDD into RDD of Java objects.
> 
>   2. Keys and values of this Java RDD are converted to Writables and written out.
> 
> 


New in version 1.1.0.

Parameters
    

**path** str
    

path to sequence file

**compressionCodecClass** str, optional
    

fully qualified classname of the compression codec class i.e. âorg.apache.hadoop.io.compress.GzipCodecâ (None by default)

See also

[`SparkContext.sequenceFile()`](pyspark.SparkContext.sequenceFile.html#pyspark.SparkContext.sequenceFile "pyspark.SparkContext.sequenceFile")
    
[`RDD.saveAsHadoopFile()`](pyspark.RDD.saveAsHadoopFile.html#pyspark.RDD.saveAsHadoopFile "pyspark.RDD.saveAsHadoopFile")
    
[`RDD.saveAsNewAPIHadoopFile()`](pyspark.RDD.saveAsNewAPIHadoopFile.html#pyspark.RDD.saveAsNewAPIHadoopFile "pyspark.RDD.saveAsNewAPIHadoopFile")
    
[`RDD.saveAsHadoopDataset()`](pyspark.RDD.saveAsHadoopDataset.html#pyspark.RDD.saveAsHadoopDataset "pyspark.RDD.saveAsHadoopDataset")
    
[`RDD.saveAsNewAPIHadoopDataset()`](pyspark.RDD.saveAsNewAPIHadoopDataset.html#pyspark.RDD.saveAsNewAPIHadoopDataset "pyspark.RDD.saveAsNewAPIHadoopDataset")
    
`RDD.saveAsSequenceFile()`
    

Examples
    
    
    >>> import os
    >>> import tempfile
    

Set the related classes
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsSequenceFile") as d:
    ...     path = os.path.join(d, "sequence_file")
    ...
    ...     # Write a temporary sequence file
    ...     rdd = sc.parallelize([(1, ""), (1, "a"), (3, "x")])
    ...     rdd.saveAsSequenceFile(path)
    ...
    ...     # Load this sequence file as an RDD
    ...     loaded = sc.sequenceFile(path)
    ...     sorted(loaded.collect())
    [(1, ''), (1, 'a'), (3, 'x')]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsSequenceFile.rst.txt)


---

## 🔹 179. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.saveAsTextFile.html

# pyspark.RDD.saveAsTextFile#

RDD.saveAsTextFile(_path_ , _compressionCodecClass =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.saveAsTextFile)#
    

Save this RDD as a text file, using string representations of elements.

New in version 0.7.0.

Parameters
    

**path** str
    

path to text file

**compressionCodecClass** str, optional
    

fully qualified classname of the compression codec class i.e. âorg.apache.hadoop.io.compress.GzipCodecâ (None by default)

See also

[`SparkContext.textFile()`](pyspark.SparkContext.textFile.html#pyspark.SparkContext.textFile "pyspark.SparkContext.textFile")
    
[`SparkContext.wholeTextFiles()`](pyspark.SparkContext.wholeTextFiles.html#pyspark.SparkContext.wholeTextFiles "pyspark.SparkContext.wholeTextFiles")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> from fileinput import input
    >>> from glob import glob
    >>> with tempfile.TemporaryDirectory(prefix="saveAsTextFile1") as d1:
    ...     path1 = os.path.join(d1, "text_file1")
    ...
    ...     # Write a temporary text file
    ...     sc.parallelize(range(10)).saveAsTextFile(path1)
    ...
    ...     # Load text file as an RDD
    ...     ''.join(sorted(input(glob(path1 + "/part-0000*"))))
    '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    

Empty lines are tolerated when saving to text files.
    
    
    >>> with tempfile.TemporaryDirectory(prefix="saveAsTextFile2") as d2:
    ...     path2 = os.path.join(d2, "text2_file2")
    ...
    ...     # Write another temporary text file
    ...     sc.parallelize(['', 'foo', '', 'bar', '']).saveAsTextFile(path2)
    ...
    ...     # Load text file as an RDD
    ...     ''.join(sorted(input(glob(path2 + "/part-0000*"))))
    '\n\n\nbar\nfoo\n'
    

Using compressionCodecClass
    
    
    >>> from fileinput import input, hook_compressed
    >>> with tempfile.TemporaryDirectory(prefix="saveAsTextFile3") as d3:
    ...     path3 = os.path.join(d3, "text3")
    ...     codec = "org.apache.hadoop.io.compress.GzipCodec"
    ...
    ...     # Write another temporary text file with specified codec
    ...     sc.parallelize(['foo', 'bar']).saveAsTextFile(path3, codec)
    ...
    ...     # Load text file as an RDD
    ...     result = sorted(input(glob(path3 + "/part*.gz"), openhook=hook_compressed))
    ...     ''.join([r.decode('utf-8') if isinstance(r, bytes) else r for r in result])
    'bar\nfoo\n'
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.saveAsTextFile.rst.txt)


---

## 🔹 180. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.setName.html

# pyspark.RDD.setName#

RDD.setName(_name_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.setName)#
    

Assign a name to this RDD.

New in version 1.0.0.

Parameters
    

**name** str
    

new name

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

the same [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with name updated

See also

[`RDD.name()`](pyspark.RDD.name.html#pyspark.RDD.name "pyspark.RDD.name")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 2])
    >>> rdd.setName('I am an RDD').name()
    'I am an RDD'
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.setName.rst.txt)


---

## 🔹 181. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sortBy.html

# pyspark.RDD.sortBy#

RDD.sortBy(_keyfunc_ , _ascending =True_, _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.sortBy)#
    

Sorts this RDD by the given keyfunc

New in version 1.1.0.

Parameters
    

**keyfunc** function
    

a function to compute the key

**ascending** bool, optional, default True
    

sort the keys in ascending or descending order

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

See also

[`RDD.sortByKey()`](pyspark.RDD.sortByKey.html#pyspark.RDD.sortByKey "pyspark.RDD.sortByKey")
    
[`pyspark.sql.DataFrame.sort()`](../pyspark.sql/api/pyspark.sql.DataFrame.sort.html#pyspark.sql.DataFrame.sort "pyspark.sql.DataFrame.sort")
    

Examples
    
    
    >>> tmp = [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
    >>> sc.parallelize(tmp).sortBy(lambda x: x[0]).collect()
    [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
    >>> sc.parallelize(tmp).sortBy(lambda x: x[1]).collect()
    [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sortBy.rst.txt)


---

## 🔹 182. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sortByKey.html

# pyspark.RDD.sortByKey#

RDD.sortByKey(_ascending=True_ , _numPartitions=None_ , _keyfunc= <function RDD.<lambda>>_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.sortByKey)#
    

Sorts this RDD, which is assumed to consist of (key, value) pairs.

New in version 0.9.1.

Parameters
    

**ascending** bool, optional, default True
    

sort the keys in ascending or descending order

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**keyfunc** function, optional, default identity mapping
    

a function to compute the key

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

See also

[`RDD.sortBy()`](pyspark.RDD.sortBy.html#pyspark.RDD.sortBy "pyspark.RDD.sortBy")
    
[`pyspark.sql.DataFrame.sort()`](../pyspark.sql/api/pyspark.sql.DataFrame.sort.html#pyspark.sql.DataFrame.sort "pyspark.sql.DataFrame.sort")
    

Examples
    
    
    >>> tmp = [('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)]
    >>> sc.parallelize(tmp).sortByKey().first()
    ('1', 3)
    >>> sc.parallelize(tmp).sortByKey(True, 1).collect()
    [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
    >>> sc.parallelize(tmp).sortByKey(True, 2).collect()
    [('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)]
    >>> tmp2 = [('Mary', 1), ('had', 2), ('a', 3), ('little', 4), ('lamb', 5)]
    >>> tmp2.extend([('whose', 6), ('fleece', 7), ('was', 8), ('white', 9)])
    >>> sc.parallelize(tmp2).sortByKey(True, 3, keyfunc=lambda k: k.lower()).collect()
    [('a', 3), ('fleece', 7), ('had', 2), ('lamb', 5),...('white', 9), ('whose', 6)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sortByKey.rst.txt)


---

## 🔹 183. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.stats.html

# pyspark.RDD.stats#

RDD.stats()[[source]](../../_modules/pyspark/core/rdd.html#RDD.stats)#
    

Return a `StatCounter` object that captures the mean, variance and count of the RDDâs elements in one operation.

New in version 0.9.1.

Returns
    

`StatCounter`
    

a `StatCounter` capturing the mean, variance and count of all elements

See also

[`RDD.stdev()`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")
    
[`RDD.sampleStdev()`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")
    
[`RDD.variance()`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")
    
[`RDD.sampleVariance()`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")
    
[`RDD.histogram()`](pyspark.RDD.histogram.html#pyspark.RDD.histogram "pyspark.RDD.histogram")
    
[`pyspark.sql.DataFrame.stat()`](../pyspark.sql/api/pyspark.sql.DataFrame.stat.html#pyspark.sql.DataFrame.stat "pyspark.sql.DataFrame.stat")
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.stats.rst.txt)


---

## 🔹 184. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.stdev.html

# pyspark.RDD.stdev#

RDD.stdev()[[source]](../../_modules/pyspark/core/rdd.html#RDD.stdev)#
    

Compute the standard deviation of this RDDâs elements.

New in version 0.9.1.

Returns
    

float
    

the standard deviation of all elements

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    
[`RDD.sampleStdev()`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")
    
[`RDD.variance()`](pyspark.RDD.variance.html#pyspark.RDD.variance "pyspark.RDD.variance")
    
[`RDD.sampleVariance()`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3]).stdev()
    0.816...
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.stdev.rst.txt)


---

## 🔹 185. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.subtract.html

# pyspark.RDD.subtract#

RDD.subtract(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.subtract)#
    

Return each value in self that is not contained in other.

New in version 0.9.1.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with the elements from this that are not in other

See also

[`RDD.subtractByKey()`](pyspark.RDD.subtractByKey.html#pyspark.RDD.subtractByKey "pyspark.RDD.subtractByKey")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 3)])
    >>> rdd2 = sc.parallelize([("a", 3), ("c", None)])
    >>> sorted(rdd1.subtract(rdd2).collect())
    [('a', 1), ('b', 4), ('b', 5)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.subtract.rst.txt)


---

## 🔹 186. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.subtractByKey.html

# pyspark.RDD.subtractByKey#

RDD.subtractByKey(_other_ , _numPartitions =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.subtractByKey)#
    

Return each (key, value) pair in self that has no pair with matching key in other.

New in version 0.9.1.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

**numPartitions** int, optional
    

the number of partitions in new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with the pairs from this whose keys are not in other

See also

[`RDD.subtract()`](pyspark.RDD.subtract.html#pyspark.RDD.subtract "pyspark.RDD.subtract")
    

Examples
    
    
    >>> rdd1 = sc.parallelize([("a", 1), ("b", 4), ("b", 5), ("a", 2)])
    >>> rdd2 = sc.parallelize([("a", 3), ("c", None)])
    >>> sorted(rdd1.subtractByKey(rdd2).collect())
    [('b', 4), ('b', 5)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.subtractByKey.rst.txt)


---

## 🔹 187. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sum.html

# pyspark.RDD.sum#

RDD.sum()[[source]](../../_modules/pyspark/core/rdd.html#RDD.sum)#
    

Add up the elements in this RDD.

New in version 0.7.0.

Returns
    

float, int, or complex
    

the sum of all elements

See also

[`RDD.mean()`](pyspark.RDD.mean.html#pyspark.RDD.mean "pyspark.RDD.mean")
    
[`RDD.sumApprox()`](pyspark.RDD.sumApprox.html#pyspark.RDD.sumApprox "pyspark.RDD.sumApprox")
    

Examples
    
    
    >>> sc.parallelize([1.0, 2.0, 3.0]).sum()
    6.0
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sum.rst.txt)


---

## 🔹 188. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.sumApprox.html

# pyspark.RDD.sumApprox#

RDD.sumApprox(_timeout_ , _confidence =0.95_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.sumApprox)#
    

Approximate operation to return the sum within a timeout or meet the confidence.

New in version 1.2.0.

Parameters
    

**timeout** int
    

maximum time to wait for the job, in milliseconds

**confidence** float
    

the desired statistical confidence in the result

Returns
    

`BoundedFloat`
    

a potentially incomplete result, with error bounds

See also

[`RDD.sum()`](pyspark.RDD.sum.html#pyspark.RDD.sum "pyspark.RDD.sum")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(1000), 10)
    >>> r = sum(range(1000))
    >>> abs(rdd.sumApprox(1000) - r) / r < 0.05
    True
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.sumApprox.rst.txt)


---

## 🔹 189. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.take.html

# pyspark.RDD.take#

RDD.take(_num_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.take)#
    

Take the first num elements of the RDD.

It works by first scanning one partition, and use the results from that partition to estimate the number of additional partitions needed to satisfy the limit.

Translated from the Scala implementation in RDD#take().

New in version 0.7.0.

Parameters
    

**num** int
    

first number of elements

Returns
    

list
    

the first num elements

See also

[`RDD.first()`](pyspark.RDD.first.html#pyspark.RDD.first "pyspark.RDD.first")
    
[`pyspark.sql.DataFrame.take()`](../pyspark.sql/api/pyspark.sql.DataFrame.take.html#pyspark.sql.DataFrame.take "pyspark.sql.DataFrame.take")
    

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driverâs memory.

Examples
    
    
    >>> sc.parallelize([2, 3, 4, 5, 6]).cache().take(2)
    [2, 3]
    >>> sc.parallelize([2, 3, 4, 5, 6]).take(10)
    [2, 3, 4, 5, 6]
    >>> sc.parallelize(range(100), 100).filter(lambda x: x > 90).take(3)
    [91, 92, 93]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.take.rst.txt)


---

## 🔹 190. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.takeOrdered.html

# pyspark.RDD.takeOrdered#

RDD.takeOrdered(_num_ , _key =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.takeOrdered)#
    

Get the N elements from an RDD ordered in ascending order or as specified by the optional key function.

New in version 1.0.0.

Parameters
    

**num** int
    

top N

**key** function, optional
    

a function used to generate key for comparing

Returns
    

list
    

the top N elements

See also

[`RDD.top()`](pyspark.RDD.top.html#pyspark.RDD.top "pyspark.RDD.top")
    
[`RDD.max()`](pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")
    
[`RDD.min()`](pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")
    

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driverâs memory.

Examples
    
    
    >>> sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7]).takeOrdered(6)
    [1, 2, 3, 4, 5, 6]
    >>> sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7], 2).takeOrdered(6, key=lambda x: -x)
    [10, 9, 7, 6, 5, 4]
    >>> sc.emptyRDD().takeOrdered(3)
    []
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.takeOrdered.rst.txt)


---

## 🔹 191. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.takeSample.html

# pyspark.RDD.takeSample#

RDD.takeSample(_withReplacement_ , _num_ , _seed =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.takeSample)#
    

Return a fixed-size sampled subset of this RDD.

New in version 1.3.0.

Parameters
    

**withReplacement** bool
    

whether sampling is done with replacement

**num** int
    

size of the returned sample

**seed** int, optional
    

random seed

Returns
    

list
    

a fixed-size sampled subset of this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") in an array

See also

[`RDD.sample()`](pyspark.RDD.sample.html#pyspark.RDD.sample "pyspark.RDD.sample")
    

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driverâs memory.

Examples
    
    
    >>> import sys
    >>> rdd = sc.parallelize(range(0, 10))
    >>> len(rdd.takeSample(True, 20, 1))
    20
    >>> len(rdd.takeSample(False, 5, 2))
    5
    >>> len(rdd.takeSample(False, 15, 3))
    10
    >>> sc.range(0, 10).takeSample(False, sys.maxsize)
    Traceback (most recent call last):
        ...
    ValueError: Sample size cannot be greater than ...
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.takeSample.rst.txt)


---

## 🔹 192. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.toDebugString.html

# pyspark.RDD.toDebugString#

RDD.toDebugString()[[source]](../../_modules/pyspark/core/rdd.html#RDD.toDebugString)#
    

A description of this RDD and its recursive dependencies for debugging.

New in version 1.0.0.

Returns
    

bytes
    

debugging information of this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.toDebugString()
    b'...PythonRDD...ParallelCollectionRDD...'
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.toDebugString.rst.txt)


---

## 🔹 193. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.toLocalIterator.html

# pyspark.RDD.toLocalIterator#

RDD.toLocalIterator(_prefetchPartitions =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.toLocalIterator)#
    

Return an iterator that contains all of the elements in this RDD. The iterator will consume as much memory as the largest partition in this RDD. With prefetch it may consume up to the memory of the 2 largest partitions.

New in version 1.3.0.

Parameters
    

**prefetchPartitions** bool, optional
    

If Spark should pre-fetch the next partition before it is needed.

Returns
    

`collections.abc.Iterator`
    

an iterator that contains all of the elements in this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

See also

[`RDD.collect()`](pyspark.RDD.collect.html#pyspark.RDD.collect "pyspark.RDD.collect")
    
[`pyspark.sql.DataFrame.toLocalIterator()`](../pyspark.sql/api/pyspark.sql.DataFrame.toLocalIterator.html#pyspark.sql.DataFrame.toLocalIterator "pyspark.sql.DataFrame.toLocalIterator")
    

Examples
    
    
    >>> rdd = sc.parallelize(range(10))
    >>> [x for x in rdd.toLocalIterator()]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.toLocalIterator.rst.txt)


---

## 🔹 194. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.top.html

# pyspark.RDD.top#

RDD.top(_num_ , _key =None_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.top)#
    

Get the top N elements from an RDD.

New in version 1.0.0.

Parameters
    

**num** int
    

top N

**key** function, optional
    

a function used to generate key for comparing

Returns
    

list
    

the top N elements

See also

[`RDD.takeOrdered()`](pyspark.RDD.takeOrdered.html#pyspark.RDD.takeOrdered "pyspark.RDD.takeOrdered")
    
[`RDD.max()`](pyspark.RDD.max.html#pyspark.RDD.max "pyspark.RDD.max")
    
[`RDD.min()`](pyspark.RDD.min.html#pyspark.RDD.min "pyspark.RDD.min")
    

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driverâs memory.

It returns the list sorted in descending order.

Examples
    
    
    >>> sc.parallelize([10, 4, 2, 12, 3]).top(1)
    [12]
    >>> sc.parallelize([2, 3, 4, 5, 6], 2).top(2)
    [6, 5]
    >>> sc.parallelize([10, 4, 2, 12, 3]).top(3, key=str)
    [4, 3, 2]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.top.rst.txt)


---

## 🔹 195. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.treeAggregate.html

# pyspark.RDD.treeAggregate#

RDD.treeAggregate(_zeroValue_ , _seqOp_ , _combOp_ , _depth =2_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.treeAggregate)#
    

Aggregates the elements of this RDD in a multi-level tree pattern.

New in version 1.3.0.

Parameters
    

**zeroValue** U
    

the initial value for the accumulated result of each partition

**seqOp** function
    

a function used to accumulate results within a partition

**combOp** function
    

an associative function used to combine results from different partitions

**depth** int, optional, default 2
    

suggested depth of the tree

Returns
    

U
    

the aggregated result

See also

[`RDD.aggregate()`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")
    
[`RDD.treeReduce()`](pyspark.RDD.treeReduce.html#pyspark.RDD.treeReduce "pyspark.RDD.treeReduce")
    

Examples
    
    
    >>> add = lambda x, y: x + y
    >>> rdd = sc.parallelize([-5, -4, -3, -2, -1, 1, 2, 3, 4], 10)
    >>> rdd.treeAggregate(0, add, add)
    -5
    >>> rdd.treeAggregate(0, add, add, 1)
    -5
    >>> rdd.treeAggregate(0, add, add, 2)
    -5
    >>> rdd.treeAggregate(0, add, add, 5)
    -5
    >>> rdd.treeAggregate(0, add, add, 10)
    -5
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.treeAggregate.rst.txt)


---

## 🔹 196. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.treeReduce.html

# pyspark.RDD.treeReduce#

RDD.treeReduce(_f_ , _depth =2_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.treeReduce)#
    

Reduces the elements of this RDD in a multi-level tree pattern.

New in version 1.3.0.

Parameters
    

**f** function
    

the reduce function

**depth** int, optional, default 2
    

suggested depth of the tree (default: 2)

Returns
    

T
    

the aggregated result

See also

[`RDD.reduce()`](pyspark.RDD.reduce.html#pyspark.RDD.reduce "pyspark.RDD.reduce")
    
[`RDD.aggregate()`](pyspark.RDD.aggregate.html#pyspark.RDD.aggregate "pyspark.RDD.aggregate")
    
[`RDD.treeAggregate()`](pyspark.RDD.treeAggregate.html#pyspark.RDD.treeAggregate "pyspark.RDD.treeAggregate")
    

Examples
    
    
    >>> add = lambda x, y: x + y
    >>> rdd = sc.parallelize([-5, -4, -3, -2, -1, 1, 2, 3, 4], 10)
    >>> rdd.treeReduce(add)
    -5
    >>> rdd.treeReduce(add, 1)
    -5
    >>> rdd.treeReduce(add, 2)
    -5
    >>> rdd.treeReduce(add, 5)
    -5
    >>> rdd.treeReduce(add, 10)
    -5
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.treeReduce.rst.txt)


---

## 🔹 197. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.union.html

# pyspark.RDD.union#

RDD.union(_other_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.union)#
    

Return the union of this RDD and another one.

New in version 0.7.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

the union of this [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") and another one

See also

[`SparkContext.union()`](pyspark.SparkContext.union.html#pyspark.SparkContext.union "pyspark.SparkContext.union")
    
[`pyspark.sql.DataFrame.union()`](../pyspark.sql/api/pyspark.sql.DataFrame.union.html#pyspark.sql.DataFrame.union "pyspark.sql.DataFrame.union")
    

Examples
    
    
    >>> rdd = sc.parallelize([1, 1, 2, 3])
    >>> rdd.union(rdd).collect()
    [1, 1, 2, 3, 1, 1, 2, 3]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.union.rst.txt)


---

## 🔹 198. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.unpersist.html

# pyspark.RDD.unpersist#

RDD.unpersist(_blocking =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.unpersist)#
    

Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.

New in version 0.9.1.

Parameters
    

**blocking** bool, optional, default False
    

whether to block until all blocks are deleted

New in version 3.0.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

The same [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

See also

[`RDD.cache()`](pyspark.RDD.cache.html#pyspark.RDD.cache "pyspark.RDD.cache")
    
[`RDD.persist()`](pyspark.RDD.persist.html#pyspark.RDD.persist "pyspark.RDD.persist")
    
[`RDD.getStorageLevel()`](pyspark.RDD.getStorageLevel.html#pyspark.RDD.getStorageLevel "pyspark.RDD.getStorageLevel")
    

Examples
    
    
    >>> rdd = sc.range(5)
    >>> rdd.is_cached
    False
    >>> _ = rdd.unpersist()
    >>> rdd.is_cached
    False
    >>> _ = rdd.cache()
    >>> rdd.is_cached
    True
    >>> _ = rdd.unpersist()
    >>> rdd.is_cached
    False
    >>> _ = rdd.unpersist()
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.unpersist.rst.txt)


---

## 🔹 199. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.values.html

# pyspark.RDD.values#

RDD.values()[[source]](../../_modules/pyspark/core/rdd.html#RDD.values)#
    

Return an RDD with the values of each tuple.

New in version 0.7.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") only containing the values

See also

[`RDD.keys()`](pyspark.RDD.keys.html#pyspark.RDD.keys "pyspark.RDD.keys")
    

Examples
    
    
    >>> rdd = sc.parallelize([(1, 2), (3, 4)]).values()
    >>> rdd.collect()
    [2, 4]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.values.rst.txt)


---

## 🔹 200. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.variance.html

# pyspark.RDD.variance#

RDD.variance()[[source]](../../_modules/pyspark/core/rdd.html#RDD.variance)#
    

Compute the variance of this RDDâs elements.

New in version 0.9.1.

Returns
    

float
    

the variance of all elements

See also

[`RDD.stats()`](pyspark.RDD.stats.html#pyspark.RDD.stats "pyspark.RDD.stats")
    
[`RDD.sampleVariance()`](pyspark.RDD.sampleVariance.html#pyspark.RDD.sampleVariance "pyspark.RDD.sampleVariance")
    
[`RDD.stdev()`](pyspark.RDD.stdev.html#pyspark.RDD.stdev "pyspark.RDD.stdev")
    
[`RDD.sampleStdev()`](pyspark.RDD.sampleStdev.html#pyspark.RDD.sampleStdev "pyspark.RDD.sampleStdev")
    

Examples
    
    
    >>> sc.parallelize([1, 2, 3]).variance()
    0.666...
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.variance.rst.txt)


---

## 🔹 201. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.withResources.html

# pyspark.RDD.withResources#

RDD.withResources(_profile_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.withResources)#
    

Specify a [`pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile") to use when calculating this RDD. This is only supported on certain cluster managers and currently requires dynamic allocation to be enabled. It will result in new executors with the resources specified being acquired to calculate the RDD.

New in version 3.1.0.

Parameters
    

**profile**[` pyspark.resource.ResourceProfile`](pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile")
    

a resource profile

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

the same [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") with user specified profile

See also

[`RDD.getResourceProfile()`](pyspark.RDD.getResourceProfile.html#pyspark.RDD.getResourceProfile "pyspark.RDD.getResourceProfile")
    

Notes

This API is experimental

[ __Show Source](../../_sources/reference/api/pyspark.RDD.withResources.rst.txt)


---

## 🔹 202. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.zip.html

# pyspark.RDD.zip#

RDD.zip(_other_)[[source]](../../_modules/pyspark/core/rdd.html#RDD.zip)#
    

Zips this RDD with another one, returning key-value pairs with the first element in each RDD second element in each RDD, etc. Assumes that the two RDDs have the same number of partitions and the same number of elements in each partition (e.g. one was made through a map on the other).

New in version 1.0.0.

Parameters
    

**other**[` RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

another [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the zipped key-value pairs

See also

[`RDD.zipWithIndex()`](pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex")
    
[`RDD.zipWithUniqueId()`](pyspark.RDD.zipWithUniqueId.html#pyspark.RDD.zipWithUniqueId "pyspark.RDD.zipWithUniqueId")
    

Examples
    
    
    >>> rdd1 = sc.parallelize(range(0,5))
    >>> rdd2 = sc.parallelize(range(1000, 1005))
    >>> rdd1.zip(rdd2).collect()
    [(0, 1000), (1, 1001), (2, 1002), (3, 1003), (4, 1004)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.zip.rst.txt)


---

## 🔹 203. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.zipWithIndex.html

# pyspark.RDD.zipWithIndex#

RDD.zipWithIndex()[[source]](../../_modules/pyspark/core/rdd.html#RDD.zipWithIndex)#
    

Zips this RDD with its element indices.

The ordering is first based on the partition index and then the ordering of items within each partition. So the first item in the first partition gets index 0, and the last item in the last partition receives the largest index.

This method needs to trigger a spark job when this RDD contains more than one partitions.

New in version 1.2.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the zipped key-index pairs

See also

[`RDD.zip()`](pyspark.RDD.zip.html#pyspark.RDD.zip "pyspark.RDD.zip")
    
[`RDD.zipWithUniqueId()`](pyspark.RDD.zipWithUniqueId.html#pyspark.RDD.zipWithUniqueId "pyspark.RDD.zipWithUniqueId")
    

Examples
    
    
    >>> sc.parallelize(["a", "b", "c", "d"], 3).zipWithIndex().collect()
    [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.zipWithIndex.rst.txt)


---

## 🔹 204. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.zipWithUniqueId.html

# pyspark.RDD.zipWithUniqueId#

RDD.zipWithUniqueId()[[source]](../../_modules/pyspark/core/rdd.html#RDD.zipWithUniqueId)#
    

Zips this RDD with generated unique Long ids.

Items in the kth partition will get ids k, n+k, 2*n+k, â¦, where n is the number of partitions. So there may exist gaps, but this method wonât trigger a spark job, which is different from [`zipWithIndex()`](pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex").

New in version 1.2.0.

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") containing the zipped key-UniqueId pairs

See also

[`RDD.zip()`](pyspark.RDD.zip.html#pyspark.RDD.zip "pyspark.RDD.zip")
    
[`RDD.zipWithIndex()`](pyspark.RDD.zipWithIndex.html#pyspark.RDD.zipWithIndex "pyspark.RDD.zipWithIndex")
    

Examples
    
    
    >>> sc.parallelize(["a", "b", "c", "d", "e"], 3).zipWithUniqueId().collect()
    [('a', 0), ('b', 1), ('c', 4), ('d', 2), ('e', 5)]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDD.zipWithUniqueId.rst.txt)


---

## 🔹 205. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.destroy.html

# pyspark.Broadcast.destroy#

Broadcast.destroy(_blocking =False_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast.destroy)#
    

Destroy all data and metadata related to this broadcast variable. Use this with caution; once a broadcast variable has been destroyed, it cannot be used again.

Changed in version 3.0.0: Added optional argument blocking to specify whether to block until all blocks are deleted.

Parameters
    

**blocking** bool, optional, default False
    

Whether to block until unpersisting has completed.

Examples
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    

Destroy all data and metadata related to this broadcast variable
    
    
    >>> b.destroy()
    

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.destroy.rst.txt)


---

## 🔹 206. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.dump.html

# pyspark.Broadcast.dump#

Broadcast.dump(_value_ , _f_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast.dump)#
    

Write a pickled representation of value to the open file or socket. The protocol pickle is HIGHEST_PROTOCOL.

Parameters
    

**value** T
    

Value to write.

**f**` BinaryIO`
    

File or socket where the pickled value will be stored.

Examples
    
    
    >>> import os
    >>> import tempfile
    
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    

Write a pickled representation of b to the open temp file.
    
    
    >>> with tempfile.TemporaryDirectory(prefix="dump") as d:
    ...     path = os.path.join(d, "test.txt")
    ...     with open(path, "wb") as f:
    ...         b.dump(b.value, f)
    

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.dump.rst.txt)


---

## 🔹 207. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.load.html

# pyspark.Broadcast.load#

Broadcast.load(_file_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast.load)#
    

Read a pickled representation of value from the open file or socket.

Parameters
    

**file**` BinaryIO`
    

File or socket where the pickled value will be read.

Returns
    

T
    

The object hierarchy specified therein reconstituted from the pickled representation of an object.

Examples
    
    
    >>> import os
    >>> import tempfile
    
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    >>> c = spark.sparkContext.broadcast(1)
    

Read the pickled representation of value from the open temp file.
    
    
    >>> with tempfile.TemporaryDirectory(prefix="load") as d:
    ...     path = os.path.join(d, "test.txt")
    ...     with open(path, "wb") as f:
    ...         b.dump(b.value, f)
    ...     with open(path, "rb") as f:
    ...         c.load(f)
    [1, 2, 3, 4, 5]
    

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.load.rst.txt)


---

## 🔹 208. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.load_from_path.html

# pyspark.Broadcast.load_from_path#

Broadcast.load_from_path(_path_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast.load_from_path)#
    

Read the pickled representation of an object from the open file and return the reconstituted object hierarchy specified therein.

Parameters
    

**path** str
    

File path where reads the pickled value.

Returns
    

T
    

The object hierarchy specified therein reconstituted from the pickled representation of an object.

Examples
    
    
    >>> import os
    >>> import tempfile
    
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    >>> c = spark.sparkContext.broadcast(1)
    

Read the pickled representation of value from temp file.
    
    
    >>> with tempfile.TemporaryDirectory(prefix="load_from_path") as d:
    ...     path = os.path.join(d, "test.txt")
    ...     with open(path, "wb") as f:
    ...         b.dump(b.value, f)
    ...     c.load_from_path(path)
    [1, 2, 3, 4, 5]
    

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.load_from_path.rst.txt)


---

## 🔹 209. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.unpersist.html

# pyspark.Broadcast.unpersist#

Broadcast.unpersist(_blocking =False_)[[source]](../../_modules/pyspark/core/broadcast.html#Broadcast.unpersist)#
    

Delete cached copies of this broadcast on the executors. If the broadcast is used after this is called, it will need to be re-sent to each executor.

Parameters
    

**blocking** bool, optional, default False
    

Whether to block until unpersisting has completed.

Examples
    
    
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    

Delete cached copies of this broadcast on the executors
    
    
    >>> b.unpersist()
    

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.unpersist.rst.txt)


---

## 🔹 210. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Broadcast.value.html

# pyspark.Broadcast.value#

_property _Broadcast.value#
    

Return the broadcasted value

[ __Show Source](../../_sources/reference/api/pyspark.Broadcast.value.rst.txt)


---

## 🔹 211. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Accumulator.add.html

# pyspark.Accumulator.add#

Accumulator.add(_term_)[[source]](../../_modules/pyspark/accumulators.html#Accumulator.add)#
    

Adds a term to this accumulatorâs value

[ __Show Source](../../_sources/reference/api/pyspark.Accumulator.add.rst.txt)


---

## 🔹 212. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.Accumulator.value.html

# pyspark.Accumulator.value#

_property _Accumulator.value#
    

Get the accumulatorâs value; only usable in driver program

[ __Show Source](../../_sources/reference/api/pyspark.Accumulator.value.rst.txt)


---

## 🔹 213. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.AccumulatorParam.addInPlace.html

# pyspark.AccumulatorParam.addInPlace#

AccumulatorParam.addInPlace(_value1_ , _value2_)[[source]](../../_modules/pyspark/accumulators.html#AccumulatorParam.addInPlace)#
    

Add two values of the accumulatorâs data type, returning a new value; for efficiency, can also update value1 in place and return it.

[ __Show Source](../../_sources/reference/api/pyspark.AccumulatorParam.addInPlace.rst.txt)


---

## 🔹 214. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.AccumulatorParam.zero.html

# pyspark.AccumulatorParam.zero#

AccumulatorParam.zero(_value_)[[source]](../../_modules/pyspark/accumulators.html#AccumulatorParam.zero)#
    

Provide a âzero valueâ for the type, compatible in dimensions with the provided value (e.g., a zero vector)

[ __Show Source](../../_sources/reference/api/pyspark.AccumulatorParam.zero.rst.txt)


---

## 🔹 215. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.inheritable_thread_target.html

# pyspark.inheritable_thread_target#

pyspark.inheritable_thread_target(_f =None_)[[source]](../../_modules/pyspark/util.html#inheritable_thread_target)#
    

Return thread target wrapper which is recommended to be used in PySpark when the pinned thread mode is enabled. The wrapper function, before calling original thread target, it inherits the inheritable properties specific to JVM thread such as `InheritableThreadLocal`, or thread local such as tags with Spark Connect.

When the pinned thread mode is off, it return the original `f`.

New in version 3.2.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters
    

**f** function, or `SparkSession`
    

the original thread target, or `SparkSession` if Spark Connect is being used. See the examples below.

Notes

This API is experimental.

It is important to know that it captures the local properties or tags when you decorate it whereas [`InheritableThread`](pyspark.InheritableThread.html#pyspark.InheritableThread "pyspark.InheritableThread") captures when the thread is started. Therefore, it is encouraged to decorate it when you want to capture the local properties.

For example, the local properties or tags from the current Spark context or Spark session is captured when you define a function here instead of the invocation:
    
    
    >>> @inheritable_thread_target
    ... def target_func():
    ...     pass  # your codes.
    

If you have any updates on local properties or tags afterwards, it would not be reflected to the Spark context in `target_func()`.

The example below mimics the behavior of JVM threads as close as possible:
    
    
    >>> Thread(target=inheritable_thread_target(target_func)).start()  
    

If youâre using Spark Connect or if you want to inherit the tags properly, you should explicitly provide Spark session as follows:
    
    
    >>> @inheritable_thread_target(session)  
    ... def target_func():
    ...     pass  # your codes.
    
    
    
    >>> Thread(target=inheritable_thread_target(session)(target_func)).start()  
    

[ __Show Source](../../_sources/reference/api/pyspark.inheritable_thread_target.rst.txt)


---

## 🔹 216. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.contains.html

# pyspark.SparkConf.contains#

SparkConf.contains(_key_)[[source]](../../_modules/pyspark/conf.html#SparkConf.contains)#
    

Does this configuration contain a given key?

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.contains.rst.txt)


---

## 🔹 217. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.get.html

# pyspark.SparkConf.get#

SparkConf.get(_key_ , _defaultValue =None_)[[source]](../../_modules/pyspark/conf.html#SparkConf.get)#
    

Get the configured value for some key, or return a default otherwise.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.get.rst.txt)


---

## 🔹 218. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.getAll.html

# pyspark.SparkConf.getAll#

SparkConf.getAll()[[source]](../../_modules/pyspark/conf.html#SparkConf.getAll)#
    

Get all values as a list of key-value pairs.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.getAll.rst.txt)


---

## 🔹 219. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.set.html

# pyspark.SparkConf.set#

SparkConf.set(_key_ , _value_)[[source]](../../_modules/pyspark/conf.html#SparkConf.set)#
    

Set a configuration property.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.set.rst.txt)


---

## 🔹 220. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setAll.html

# pyspark.SparkConf.setAll#

SparkConf.setAll(_pairs_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setAll)#
    

Set multiple parameters, passed as a list of key-value pairs.

Parameters
    

**pairs** iterable of tuples
    

list of key-value pairs to set

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setAll.rst.txt)


---

## 🔹 221. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setAppName.html

# pyspark.SparkConf.setAppName#

SparkConf.setAppName(_value_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setAppName)#
    

Set application name.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setAppName.rst.txt)


---

## 🔹 222. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setExecutorEnv.html

# pyspark.SparkConf.setExecutorEnv#

SparkConf.setExecutorEnv(_key =None_, _value =None_, _pairs =None_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setExecutorEnv)#
    

Set an environment variable to be passed to executors.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setExecutorEnv.rst.txt)


---

## 🔹 223. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setIfMissing.html

# pyspark.SparkConf.setIfMissing#

SparkConf.setIfMissing(_key_ , _value_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setIfMissing)#
    

Set a configuration property, if not already set.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setIfMissing.rst.txt)


---

## 🔹 224. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setMaster.html

# pyspark.SparkConf.setMaster#

SparkConf.setMaster(_value_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setMaster)#
    

Set master URL to connect to.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setMaster.rst.txt)


---

## 🔹 225. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.setSparkHome.html

# pyspark.SparkConf.setSparkHome#

SparkConf.setSparkHome(_value_)[[source]](../../_modules/pyspark/conf.html#SparkConf.setSparkHome)#
    

Set path where Spark is installed on worker nodes.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.setSparkHome.rst.txt)


---

## 🔹 226. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.toDebugString.html

# pyspark.SparkConf.toDebugString#

SparkConf.toDebugString()[[source]](../../_modules/pyspark/conf.html#SparkConf.toDebugString)#
    

Returns a printable version of the configuration, as a list of key=value pairs, one per line.

[ __Show Source](../../_sources/reference/api/pyspark.SparkConf.toDebugString.rst.txt)


---

## 🔹 227. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkFiles.get.html

# pyspark.SparkFiles.get#

_classmethod _SparkFiles.get(_filename_)[[source]](../../_modules/pyspark/core/files.html#SparkFiles.get)#
    

Get the absolute path of a file added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").

New in version 0.7.0.

Parameters
    

**filename** str
    

file that are added to resources

Returns
    

str
    

the absolute path of the file

See also

[`SparkFiles.getRootDirectory()`](pyspark.SparkFiles.getRootDirectory.html#pyspark.SparkFiles.getRootDirectory "pyspark.SparkFiles.getRootDirectory")
    
[`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")
    
[`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")
    
[`SparkContext.listFiles()`](pyspark.SparkContext.listFiles.html#pyspark.SparkContext.listFiles "pyspark.SparkContext.listFiles")
    

Examples
    
    
    >>> import os
    >>> import tempfile
    >>> from pyspark import SparkFiles
    
    
    
    >>> with tempfile.TemporaryDirectory(prefix="get") as d:
    ...     path1 = os.path.join(d, "test.txt")
    ...     with open(path1, "w") as f:
    ...         _ = f.write("100")
    ...
    ...     sc.addFile(path1)
    ...     file_list1 = sorted(sc.listFiles)
    ...
    ...     def func1(iterator):
    ...         path = SparkFiles.get("test.txt")
    ...         assert path.startswith(SparkFiles.getRootDirectory())
    ...         return [path]
    ...
    ...     path_list1 = sc.parallelize([1, 2, 3, 4]).mapPartitions(func1).collect()
    ...
    ...     path2 = os.path.join(d, "test.py")
    ...     with open(path2, "w") as f:
    ...         _ = f.write("import pyspark")
    ...
    ...     # py files
    ...     sc.addPyFile(path2)
    ...     file_list2 = sorted(sc.listFiles)
    ...
    ...     def func2(iterator):
    ...         path = SparkFiles.get("test.py")
    ...         assert path.startswith(SparkFiles.getRootDirectory())
    ...         return [path]
    ...
    ...     path_list2 = sc.parallelize([1, 2, 3, 4]).mapPartitions(func2).collect()
    >>> file_list1
    ['file:/.../test.txt']
    >>> set(path_list1)
    {'.../test.txt'}
    >>> file_list2
    ['file:/.../test.py', 'file:/.../test.txt']
    >>> set(path_list2)
    {'.../test.py'}
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkFiles.get.rst.txt)


---

## 🔹 228. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkFiles.getRootDirectory.html

# pyspark.SparkFiles.getRootDirectory#

_classmethod _SparkFiles.getRootDirectory()[[source]](../../_modules/pyspark/core/files.html#SparkFiles.getRootDirectory)#
    

Get the root directory that contains files added through [`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile") or [`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile").

New in version 0.7.0.

Returns
    

str
    

the root directory that contains files added to resources

See also

[`SparkFiles.get()`](pyspark.SparkFiles.get.html#pyspark.SparkFiles.get "pyspark.SparkFiles.get")
    
[`SparkContext.addFile()`](pyspark.SparkContext.addFile.html#pyspark.SparkContext.addFile "pyspark.SparkContext.addFile")
    
[`SparkContext.addPyFile()`](pyspark.SparkContext.addPyFile.html#pyspark.SparkContext.addPyFile "pyspark.SparkContext.addPyFile")
    

Examples
    
    
    >>> from pyspark.core.files import SparkFiles
    >>> SparkFiles.getRootDirectory()  
    '.../spark-a904728e-08d3-400c-a872-cfd82fd6dcd2/userFiles-648cf6d6-bb2c-4f53-82bd-e658aba0c5de'
    

[ __Show Source](../../_sources/reference/api/pyspark.SparkFiles.getRootDirectory.rst.txt)


---

## 🔹 229. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.DISK_ONLY.html

# pyspark.StorageLevel.DISK_ONLY#

StorageLevel.DISK_ONLY _ = StorageLevel(True, False, False, False, 1)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.DISK_ONLY.rst.txt)


---

## 🔹 230. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.DISK_ONLY_2.html

# pyspark.StorageLevel.DISK_ONLY_2#

StorageLevel.DISK_ONLY_2 _ = StorageLevel(True, False, False, False, 2)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.DISK_ONLY_2.rst.txt)


---

## 🔹 231. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.DISK_ONLY_3.html

# pyspark.StorageLevel.DISK_ONLY_3#

StorageLevel.DISK_ONLY_3 _ = StorageLevel(True, False, False, False, 3)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.DISK_ONLY_3.rst.txt)


---

## 🔹 232. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK.html

# pyspark.StorageLevel.MEMORY_AND_DISK#

StorageLevel.MEMORY_AND_DISK _ = StorageLevel(True, True, False, False, 1)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK.rst.txt)


---

## 🔹 233. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK_2.html

# pyspark.StorageLevel.MEMORY_AND_DISK_2#

StorageLevel.MEMORY_AND_DISK_2 _ = StorageLevel(True, True, False, False, 2)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK_2.rst.txt)


---

## 🔹 234. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK_DESER.html

# pyspark.StorageLevel.MEMORY_AND_DISK_DESER#

StorageLevel.MEMORY_AND_DISK_DESER _ = StorageLevel(True, True, False, True, 1)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.MEMORY_AND_DISK_DESER.rst.txt)


---

## 🔹 235. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.MEMORY_ONLY.html#

# pyspark.StorageLevel.MEMORY_ONLY#

StorageLevel.MEMORY_ONLY _ = StorageLevel(False, True, False, False, 1)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.MEMORY_ONLY.rst.txt)


---

## 🔹 236. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.MEMORY_ONLY_2.html

# pyspark.StorageLevel.MEMORY_ONLY_2#

StorageLevel.MEMORY_ONLY_2 _ = StorageLevel(False, True, False, False, 2)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.MEMORY_ONLY_2.rst.txt)


---

## 🔹 237. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.StorageLevel.OFF_HEAP.html

# pyspark.StorageLevel.OFF_HEAP#

StorageLevel.OFF_HEAP _ = StorageLevel(True, True, True, False, 1)_#
    

[ __Show Source](../../_sources/reference/api/pyspark.StorageLevel.OFF_HEAP.rst.txt)


---

## 🔹 238. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.attemptNumber.html

# pyspark.TaskContext.attemptNumber#

TaskContext.attemptNumber()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.attemptNumber)#
    

How many times this task has been attempted. The first task attempt will be assigned attemptNumber = 0, and subsequent attempts will have increasing attempt numbers.

Returns
    

int
    

current attempt number.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.attemptNumber.rst.txt)


---

## 🔹 239. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.cpus.html

# pyspark.TaskContext.cpus#

TaskContext.cpus()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.cpus)#
    

CPUs allocated to the task.

Returns
    

int
    

the number of CPUs.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.cpus.rst.txt)


---

## 🔹 240. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.get.html

# pyspark.TaskContext.get#

_classmethod _TaskContext.get()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.get)#
    

Return the currently active [`TaskContext`](pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext"). This can be called inside of user functions to access contextual information about running tasks.

Returns
    

[`TaskContext`](pyspark.TaskContext.html#pyspark.TaskContext "pyspark.TaskContext"), optional
    

Notes

Must be called on the worker, not the driver. Returns `None` if not initialized.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.get.rst.txt)


---

## 🔹 241. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.getLocalProperty.html

# pyspark.TaskContext.getLocalProperty#

TaskContext.getLocalProperty(_key_)[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.getLocalProperty)#
    

Get a local property set upstream in the driver, or None if it is missing.

Parameters
    

**key** str
    

the key of the local property to get.

Returns
    

int
    

the value of the local property.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.getLocalProperty.rst.txt)


---

## 🔹 242. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.partitionId.html

# pyspark.TaskContext.partitionId#

TaskContext.partitionId()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.partitionId)#
    

The ID of the RDD partition that is computed by this task.

Returns
    

int
    

current partition id.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.partitionId.rst.txt)


---

## 🔹 243. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.resources.html

# pyspark.TaskContext.resources#

TaskContext.resources()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.resources)#
    

Resources allocated to the task. The key is the resource name and the value is information about the resource.

Returns
    

dict
    

a dictionary of a string resource name, and `ResourceInformation`.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.resources.rst.txt)


---

## 🔹 244. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.stageId.html

# pyspark.TaskContext.stageId#

TaskContext.stageId()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.stageId)#
    

The ID of the stage that this task belong to.

Returns
    

int
    

current stage id.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.stageId.rst.txt)


---

## 🔹 245. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.TaskContext.taskAttemptId.html

# pyspark.TaskContext.taskAttemptId#

TaskContext.taskAttemptId()[[source]](../../_modules/pyspark/taskcontext.html#TaskContext.taskAttemptId)#
    

An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID). This is roughly equivalent to Hadoopâs TaskAttemptID.

Returns
    

int
    

current task attempt id.

[ __Show Source](../../_sources/reference/api/pyspark.TaskContext.taskAttemptId.rst.txt)


---

## 🔹 246. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDDBarrier.mapPartitions.html

# pyspark.RDDBarrier.mapPartitions#

RDDBarrier.mapPartitions(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDDBarrier.mapPartitions)#
    

Returns a new RDD by applying a function to each partition of the wrapped RDD, where tasks are launched together in a barrier stage. The interface is the same as [`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions"). Please see the API doc there.

New in version 2.4.0.

Parameters
    

**f** function
    

a function to run on each partition of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each partition

See also

[`RDD.mapPartitions()`](pyspark.RDD.mapPartitions.html#pyspark.RDD.mapPartitions "pyspark.RDD.mapPartitions")
    

Notes

This API is experimental

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 2)
    >>> def f(iterator): yield sum(iterator)
    ...
    >>> barrier = rdd.barrier()
    >>> barrier
    <pyspark.core.rdd.RDDBarrier ...>
    >>> barrier.mapPartitions(f).collect()
    [3, 7]
    

[ __Show Source](../../_sources/reference/api/pyspark.RDDBarrier.mapPartitions.rst.txt)


---

## 🔹 247. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDDBarrier.mapPartitionsWithIndex.html

# pyspark.RDDBarrier.mapPartitionsWithIndex#

RDDBarrier.mapPartitionsWithIndex(_f_ , _preservesPartitioning =False_)[[source]](../../_modules/pyspark/core/rdd.html#RDDBarrier.mapPartitionsWithIndex)#
    

Returns a new RDD by applying a function to each partition of the wrapped RDD, while tracking the index of the original partition. And all tasks are launched together in a barrier stage. The interface is the same as [`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex"). Please see the API doc there.

New in version 3.0.0.

Parameters
    

**f** function
    

a function to run on each partition of the RDD

**preservesPartitioning** bool, optional, default False
    

indicates whether the input function preserves the partitioner, which should be False unless this is a pair RDD and the input function doesnât modify the keys

Returns
    

[`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD")
    

a new [`RDD`](pyspark.RDD.html#pyspark.RDD "pyspark.RDD") by applying a function to each partition

See also

[`RDD.mapPartitionsWithIndex()`](pyspark.RDD.mapPartitionsWithIndex.html#pyspark.RDD.mapPartitionsWithIndex "pyspark.RDD.mapPartitionsWithIndex")
    

Notes

This API is experimental

Examples
    
    
    >>> rdd = sc.parallelize([1, 2, 3, 4], 4)
    >>> def f(splitIndex, iterator): yield splitIndex
    ...
    >>> barrier = rdd.barrier()
    >>> barrier
    <pyspark.core.rdd.RDDBarrier ...>
    >>> barrier.mapPartitionsWithIndex(f).sum()
    6
    

[ __Show Source](../../_sources/reference/api/pyspark.RDDBarrier.mapPartitionsWithIndex.rst.txt)


---

## 🔹 248. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.allGather.html

# pyspark.BarrierTaskContext.allGather#

BarrierTaskContext.allGather(_message =''_)[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext.allGather)#
    

This function blocks until all tasks in the same stage have reached this routine. Each task passes in a message and returns with a list of all the messages passed in by each of those tasks.

New in version 3.0.0.

Notes

This API is experimental

In a barrier stage, each task much have the same number of barrier() calls, in all possible code branches. Otherwise, you may get the job hanging or a SparkException after timeout.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.allGather.rst.txt)


---

## 🔹 249. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.attemptNumber.html

# pyspark.BarrierTaskContext.attemptNumber#

BarrierTaskContext.attemptNumber()#
    

How many times this task has been attempted. The first task attempt will be assigned attemptNumber = 0, and subsequent attempts will have increasing attempt numbers.

Returns
    

int
    

current attempt number.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.attemptNumber.rst.txt)


---

## 🔹 250. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.barrier.html

# pyspark.BarrierTaskContext.barrier#

BarrierTaskContext.barrier()[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext.barrier)#
    

Sets a global barrier and waits until all tasks in this stage hit this barrier. Similar to MPI_Barrier function in MPI, this function blocks until all tasks in the same stage have reached this routine.

New in version 2.4.0.

Notes

This API is experimental

In a barrier stage, each task much have the same number of barrier() calls, in all possible code branches. Otherwise, you may get the job hanging or a SparkException after timeout.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.barrier.rst.txt)


---

## 🔹 251. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.cpus.html

# pyspark.BarrierTaskContext.cpus#

BarrierTaskContext.cpus()#
    

CPUs allocated to the task.

Returns
    

int
    

the number of CPUs.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.cpus.rst.txt)


---

## 🔹 252. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.get.html

# pyspark.BarrierTaskContext.get#

_classmethod _BarrierTaskContext.get()[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext.get)#
    

Return the currently active [`BarrierTaskContext`](pyspark.BarrierTaskContext.html#pyspark.BarrierTaskContext "pyspark.BarrierTaskContext"). This can be called inside of user functions to access contextual information about running tasks.

Notes

Must be called on the worker, not the driver. Returns `None` if not initialized. An Exception will raise if it is not in a barrier stage.

This API is experimental

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.get.rst.txt)


---

## 🔹 253. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.getLocalProperty.html

# pyspark.BarrierTaskContext.getLocalProperty#

BarrierTaskContext.getLocalProperty(_key_)#
    

Get a local property set upstream in the driver, or None if it is missing.

Parameters
    

**key** str
    

the key of the local property to get.

Returns
    

int
    

the value of the local property.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.getLocalProperty.rst.txt)


---

## 🔹 254. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.getTaskInfos.html

# pyspark.BarrierTaskContext.getTaskInfos#

BarrierTaskContext.getTaskInfos()[[source]](../../_modules/pyspark/taskcontext.html#BarrierTaskContext.getTaskInfos)#
    

Returns [`BarrierTaskInfo`](pyspark.BarrierTaskInfo.html#pyspark.BarrierTaskInfo "pyspark.BarrierTaskInfo") for all tasks in this barrier stage, ordered by partition ID.

New in version 2.4.0.

Notes

This API is experimental

Examples
    
    
    >>> from pyspark import BarrierTaskContext
    >>> rdd = spark.sparkContext.parallelize([1])
    >>> barrier_info = rdd.barrier().mapPartitions(
    ...     lambda _: [BarrierTaskContext.get().getTaskInfos()]).collect()[0][0]
    >>> barrier_info.address
    '...:...'
    

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.getTaskInfos.rst.txt)


---

## 🔹 255. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.partitionId.html

# pyspark.BarrierTaskContext.partitionId#

BarrierTaskContext.partitionId()#
    

The ID of the RDD partition that is computed by this task.

Returns
    

int
    

current partition id.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.partitionId.rst.txt)


---

## 🔹 256. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.resources.html

# pyspark.BarrierTaskContext.resources#

BarrierTaskContext.resources()#
    

Resources allocated to the task. The key is the resource name and the value is information about the resource.

Returns
    

dict
    

a dictionary of a string resource name, and `ResourceInformation`.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.resources.rst.txt)


---

## 🔹 257. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.stageId.html

# pyspark.BarrierTaskContext.stageId#

BarrierTaskContext.stageId()#
    

The ID of the stage that this task belong to.

Returns
    

int
    

current stage id.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.stageId.rst.txt)


---

## 🔹 258. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.BarrierTaskContext.taskAttemptId.html

# pyspark.BarrierTaskContext.taskAttemptId#

BarrierTaskContext.taskAttemptId()#
    

An ID that is unique to this task attempt (within the same [`SparkContext`](pyspark.SparkContext.html#pyspark.SparkContext "pyspark.SparkContext"), no two task attempts will share the same attempt ID). This is roughly equivalent to Hadoopâs TaskAttemptID.

Returns
    

int
    

current task attempt id.

[ __Show Source](../../_sources/reference/api/pyspark.BarrierTaskContext.taskAttemptId.rst.txt)


---

## 🔹 259. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.util.VersionUtils.majorMinorVersion.html

# pyspark.util.VersionUtils.majorMinorVersion#

_static _VersionUtils.majorMinorVersion(_sparkVersion_)[[source]](../../_modules/pyspark/util.html#VersionUtils.majorMinorVersion)#
    

Given a Spark version string, return the (major version number, minor version number). E.g., for 2.0.1-SNAPSHOT, return (2, 0).

Examples
    
    
    >>> sparkVersion = "2.4.0"
    >>> VersionUtils.majorMinorVersion(sparkVersion)
    (2, 4)
    >>> sparkVersion = "2.3.0-SNAPSHOT"
    >>> VersionUtils.majorMinorVersion(sparkVersion)
    (2, 3)
    

[ __Show Source](../../_sources/reference/api/pyspark.util.VersionUtils.majorMinorVersion.rst.txt)
