# Databricks notebook source
print("Hello world!")

# COMMAND ----------



# COMMAND ----------

2+2

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC
# MAGIC `Hi!`

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello"

# COMMAND ----------

# MAGIC %fs ls "/databricks-datasets"

# COMMAND ----------

dbutils.help()

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets/"))

# COMMAND ----------



# COMMAND ----------

# MAGIC %run ./subfolder_training_folder_v1/trainig_config_notebook

# COMMAND ----------

full_name

# COMMAND ----------

API_KEY
