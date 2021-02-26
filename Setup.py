import cx_Freeze

executables =  [cx_Freeze.Executable("Obstaclimb.py")]
cx_Freeze.setup(
    name="Obstaclimb",
    options={"build_exe": {"packages":["pygame"],"include_files":["account_choose.png","account_delete.png",
                                                                    "account_deleted.png","account_limit.png",
                                                                    "account_select.png","crear_cuenta.png","cuenta.png",
                                                                    "data.txt","elegir_cuenta.png","icono.png","jugar.png",
                                                                    "noaccount.png","titulo.png"]}},
    executables = executables
    )
