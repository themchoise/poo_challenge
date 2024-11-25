import json
ETL_STATUS_FILE = "markerian-coscarelli-mele-vanotti-joyce/etl_status.json"
def check_etk_status():
    try:
        with open(ETL_STATUS_FILE, "r") as file:
            status_from_file = json.load(file)
            status_etl = status_from_file.get("etl_executed")  
        return status_etl
    except FileNotFoundError:
        print(f"El archivo {ETL_STATUS_FILE} no existe. Asegúrate de que la ruta sea correcta.")
    except json.JSONDecodeError:
        print(f"Hubo un error al leer el archivo JSON. Asegúrate de que el archivo esté bien formateado.")
    status_p =   ' Ya ejecutado' if status_etl else ' No ejecutado'
    print(f'Estado de ejecucion del ETL { status_p   }')

def set_etl():
    with open(ETL_STATUS_FILE, "w") as file:
     json.dump({"etl_executed": True}, file)

def reset_etl():
    with open(ETL_STATUS_FILE, "w") as file:
     json.dump({"etl_executed": False}, file)     