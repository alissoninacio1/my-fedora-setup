import os

# Caminho para a pasta onde estão os scripts
scripts_folder = os.path.expanduser('~/MyFedoraSetup')

# Atualizar todos os scripts na pasta MyFedoraSetup
for script_name in os.listdir(scripts_folder):
    script_path = os.path.join(scripts_folder, script_name)
    if os.path.isfile(script_path) and script_name.endswith('.sh'):
        print(f'Updating script: {script_name}')
        # Aqui você pode adicionar os comandos para atualizar cada script
        # Exemplo: os.system(f'cp /path/to/new/script.sh {script_path}')

print("Update completed.")
