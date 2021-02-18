# Databricks notebook source
import datetime
print ("This was last run on: %s" % datetime.datetime.now())

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets/samples/docs/"))

# COMMAND ----------

textFile = sc.textFile("/databricks-datasets/samples/docs/README.md")

# COMMAND ----------

textFile.count()

# COMMAND ----------

textFile.first()

# COMMAND ----------

linesWithSpark = textFile.filter(lambda line: "Spark" in line)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/"
