from claseRepositorioPersonasJSON import RespositorioPersonas
from vistaPersonas import PersonasView
from claseControladorPersonas import ControladorPersonas
from claseObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('personas.json')
    repo=RespositorioPersonas(conn)
    vista=PersonasView()
    ctrl=ControladorPersonas(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()
