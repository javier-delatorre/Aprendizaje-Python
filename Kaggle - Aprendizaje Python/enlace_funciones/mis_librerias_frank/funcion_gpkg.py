import geopandas as gpd

    # Rutas del GeoPackage y el nuevo archivo de salida

geopackage_entrada = "ruta/a/tu/geopackage.gpkg"
capa_entrada = "nombre_de_tu_capa" # Nombre de la tabla dentro del geopackage

    # Nombre del campo por el que quieres separar los registros (por ejemplo, 'tipo')
campo_separacion = "tipo"

    # Lee el GeoPackage
gdf = gpd.read_file(geopackage_entrada, layer=capa_entrada)

    # Obtiene los valores únicos del campo de separación
valores_unicos = gdf[campo_separacion].unique()

    # Itera sobre cada valor único y guarda un nuevo GeoPackage
for valor in valores_unicos:
        # Filtra los registros para ese valor
    gdf_filtrado = gdf[gdf[campo_separacion] == valor]

        # Define la ruta para el nuevo archivo GeoPackage de salida
        # Asegúrate de que 'valor' no contenga caracteres que no se puedan usar en nombres de archivo
nombre_archivo_salida = f"ruta/a/tu/geopackage_separado_{valor}.gpkg"

        # Guarda los registros filtrados en un nuevo GeoPackage
gdf_filtrado.to_file(nombre_archivo_salida, driver="GPKG")

print(f"Se ha creado el archivo '{nombre_archivo_salida}' con los registros de tipo '{valor}'.")