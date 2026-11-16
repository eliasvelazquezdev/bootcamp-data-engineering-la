# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %md
# MAGIC # Ejercicios SQL Base — Semana 1
# MAGIC ## Fundamentos de Ingeniería de Datos
# MAGIC
# MAGIC **Bootcamp:** Fundamentos de Ingeniería de Datos
# MAGIC **Dataset:** `samples.nyctaxi.trips`
# MAGIC **Instructor:** Luciano Argolo — [lucianoargolo.com](https://lucianoargolo.com)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC **Instrucciones:**
# MAGIC 1. Importá este notebook en tu Workspace de Databricks
# MAGIC 2. Conectá un cluster (se enciende automáticamente)
# MAGIC 3. Resolvé cada ejercicio en la celda SQL vacía debajo de cada consigna
# MAGIC 4. Las pistas y soluciones están en la plataforma (pestaña Solución, después de revelar las 3 pistas)
# MAGIC
# MAGIC **Numeración:** Cada ejercicio tiene un número (ej: 1.1, 2.3) que coincide con el de la plataforma para que puedas encontrar la solución fácilmente.

# COMMAND ----------

# MAGIC %md
# MAGIC # PARTE 1: Primeros pasos en Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 1.1 — Tu primera query
# MAGIC
# MAGIC **Objetivo:** Verificar que tu entorno funciona ejecutando tu primera query.
# MAGIC **Pregunta:** ¿Cuántos viajes hay en total en el dataset de NYC Taxi Trips?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 1.1: Tu solución acá
# MAGIC SELECT COUNT(*)
# MAGIC FROM samples.nyctaxi.trips;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 1.2 — Explorar la estructura
# MAGIC
# MAGIC **Objetivo:** Entender qué columnas tiene el dataset y sus tipos de datos.
# MAGIC **Pregunta:** ¿Qué columnas tiene la tabla `samples.nyctaxi.trips`?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 1.2: Tu solución acá
# MAGIC SELECT *
# MAGIC FROM samples.nyctaxi.trips
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 1.3 — Viajes más largos y más cortos
# MAGIC
# MAGIC **Objetivo:** Encontrar valores extremos para validar la calidad de los datos.
# MAGIC **Pregunta:** ¿Cuál es la distancia máxima y mínima de los viajes? (excluí distancias en cero)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 1.3: Tu solución acá
# MAGIC SELECT
# MAGIC     MIN(trip_distance) AS min_trip_distance,
# MAGIC     MAX(trip_distance) AS max_trip_distance
# MAGIC FROM samples.nyctaxi.trips
# MAGIC WHERE trip_distance > 0;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 1.4 — Promedios del dataset
# MAGIC
# MAGIC **Objetivo:** Obtener un resumen estadístico básico.
# MAGIC **Pregunta:** ¿Cuál es el promedio de tarifa y el promedio de distancia? Redondeá a 2 decimales.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 1.4: Tu solución acá
# MAGIC SELECT
# MAGIC     ROUND(AVG(fare_amount), 2) AS avg_fare ,
# MAGIC     ROUND(AVG(trip_distance), 2) AS avg_distance
# MAGIC FROM samples.nyctaxi.trips;

# COMMAND ----------

# MAGIC %md
# MAGIC # PARTE 2: Filtros, condiciones y agregaciones

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2.1 — Filtrar viajes por distancia
# MAGIC
# MAGIC **Objetivo:** Aplicar filtros simples con WHERE.
# MAGIC **Pregunta:** Mostrá fecha de pickup, distancia y tarifa de todos los viajes con distancia mayor a 10 millas.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 2.1: Tu solución acá
# MAGIC SELECT tpep_pickup_datetime, trip_distance, fare_amount
# MAGIC FROM samples.nyctaxi.trips
# MAGIC WHERE trip_distance > 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2.2 — Combinar filtros con AND y OR
# MAGIC
# MAGIC **Objetivo:** Combinar condiciones lógicas.
# MAGIC **Pregunta:** Mostrá viajes con distancia > 20 millas O tarifa > $100. Incluí fecha, distancia y tarifa.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 2.2: Tu solución acá
# MAGIC SELECT 
# MAGIC     tpep_pickup_datetime,
# MAGIC     tpep_dropoff_datetime,
# MAGIC     trip_distance,
# MAGIC     fare_amount
# MAGIC FROM samples.nyctaxi.trips
# MAGIC WHERE trip_distance > 20
# MAGIC     OR fare_amount > 100;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2.3 — Filtrar con BETWEEN e IN
# MAGIC
# MAGIC **Objetivo:** Combinar rangos y listas de valores.
# MAGIC **Pregunta:** Mostrá viajes con tarifa entre $10 y $20 que salgan de los códigos postales 10009, 10013 o 10014.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 2.3: Tu solución acá
# MAGIC SELECT *
# MAGIC FROM samples.nyctaxi.trips
# MAGIC WHERE fare_amount BETWEEN 10 AND 20
# MAGIC     AND pickup_zip IN (10009, 10013, 10014)
# MAGIC     AND dropoff_zip IN (10009, 10013, 10014);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2.4 — Estadísticas globales
# MAGIC
# MAGIC **Objetivo:** Calcular totales y promedios del dataset completo.
# MAGIC **Pregunta:** Calculá el total de tarifas, la distancia total, el promedio de tarifa y el promedio de distancia. Redondeá a 2 decimales.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 2.4: Tu solución acá
# MAGIC SELECT
# MAGIC     SUM(fare_amount) AS total_fare_amounts,
# MAGIC     SUM(trip_distance) AS total_trip_distance,
# MAGIC     ROUND(AVG(fare_amount), 2) AS avg_fare_amount,
# MAGIC     ROUND(AVG(trip_distance), 2) AS avg_trip_distance
# MAGIC FROM samples.nyctaxi.trips
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 2.5 — Extremos del dataset
# MAGIC
# MAGIC **Objetivo:** Validar calidad de datos encontrando valores extremos.
# MAGIC **Pregunta:** ¿Cuál es la tarifa mínima, máxima, distancia mínima y máxima? Excluí valores en cero.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 2.5: Tu solución acá
# MAGIC SELECT
# MAGIC     MIN(fare_amount) AS min_fare_amount,
# MAGIC     MAX(fare_amount) AS max_fare_amount,
# MAGIC     MIN(trip_distance) AS min_trip_distance,
# MAGIC     MAX(trip_distance) AS max_trip_distance
# MAGIC FROM samples.nyctaxi.trips
# MAGIC WHERE fare_amount > 0 
# MAGIC     AND trip_distance > 0;

# COMMAND ----------

# MAGIC %md
# MAGIC # PARTE 3: GROUP BY y HAVING

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 3.1 — Viajes por zona de inicio
# MAGIC
# MAGIC **Objetivo:** Agrupar datos y calcular métricas por grupo.
# MAGIC **Pregunta:** Mostrá el pickup_zip, la cantidad de viajes, el ingreso total y la tarifa promedio por zona. Ordená por ingreso total de mayor a menor.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 3.1: Tu solución acá
# MAGIC SELECT
# MAGIC     pickup_zip,
# MAGIC     COUNT(*) AS total_trips,
# MAGIC     SUM(fare_amount) AS total_fare_amount,
# MAGIC     ROUND(AVG(fare_amount),2) AS avg_fare_amount
# MAGIC FROM samples.nyctaxi.trips
# MAGIC GROUP BY pickup_zip
# MAGIC ORDER BY total_trips DESC;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 3.2 — Patrones por día de la semana
# MAGIC
# MAGIC **Objetivo:** Analizar patrones temporales con funciones de fecha.
# MAGIC **Pregunta:** Mostrá la cantidad de viajes y la distancia promedio por día de la semana. Usá DAYOFWEEK(). Filtrá viajes con distancia > 0.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 3.2: Tu solución acá
# MAGIC SELECT
# MAGIC     DAYOFWEEK(tpep_pickup_datetime) AS day_of_week,
# MAGIC     COUNT(*) AS total_trips,
# MAGIC     ROUND(AVG(trip_distance), 2) AS avg_distance
# MAGIC FROM samples.nyctaxi.trips
# MAGIC GROUP BY DAYOFWEEK(tpep_pickup_datetime)
# MAGIC HAVING avg_distance > 0;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 3.3 — Análisis por hora del día
# MAGIC
# MAGIC **Objetivo:** Analizar patrones horarios.
# MAGIC **Pregunta:** Mostrá la hora del día, cantidad de viajes y tarifa promedio por hora. Ordená por hora.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 3.3: Tu solución acá
# MAGIC SELECT
# MAGIC     HOUR(tpep_pickup_datetime) AS hour_of_day,
# MAGIC     COUNT(*) AS total_trips,
# MAGIC     ROUND(AVG(fare_amount), 2) AS avg_fare
# MAGIC FROM samples.nyctaxi.trips
# MAGIC GROUP BY hour_of_day
# MAGIC ORDER BY hour_of_day;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 3.4 — Zonas de alto tráfico (HAVING)
# MAGIC
# MAGIC **Objetivo:** Filtrar grupos después de agrupar.
# MAGIC **Pregunta:** Mostrá solo las zonas que tienen más de 1,000 viajes. Ordená por cantidad de viajes de mayor a menor.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 3.4: Tu solución acá
# MAGIC SELECT 
# MAGIC     pickup_zip,
# MAGIC     COUNT(*) AS total_trips
# MAGIC FROM samples.nyctaxi.trips
# MAGIC GROUP BY pickup_zip
# MAGIC HAVING total_trips > 1000
# MAGIC ORDER BY total_trips DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Ejercicio 3.5 — Días con alta actividad (WHERE + GROUP BY + HAVING)
# MAGIC
# MAGIC **Objetivo:** Combinar GROUP BY + HAVING + ORDER BY.
# MAGIC **Pregunta:** Mostrá la fecha, cantidad de viajes y tarifa promedio de los días que tuvieron más de 200 viajes. Ordená por fecha descendente.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Ejercicio 3.5: Tu solución acá
# MAGIC SELECT
# MAGIC     DATE(tpep_pickup_datetime) AS pickup_date,
# MAGIC     COUNT(*) AS total_trips,
# MAGIC     ROUND(AVG(fare_amount),2) AS avg_fare
# MAGIC FROM samples.nyctaxi.trips
# MAGIC GROUP BY pickup_date
# MAGIC HAVING total_trips > 200
# MAGIC ORDER BY pickup_date DESC;
# MAGIC