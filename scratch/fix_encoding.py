import os

def fix_encoding(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Mapeamento de corrupções comuns de UTF-8 em Latin-1
    replacements = {
        'Ã©': 'é',
        'Ã£': 'ã',
        'Ãª': 'ê',
        'Ã§': 'ç',
        'Ã¡': 'á',
        'Ã­': 'í',
        'Ãº': 'ú',
        'Ãµ': 'õ',
        'Ã ': 'à',
        'Ã¢': 'â',
        'Ã³': 'ó',
        'Ã´': 'ô',
        'â€”': '—',
        'Ã_': 'í', # Caso comum de erro em 'início'
        'Ã³': 'ó',
        'Ãš': 'Ú',
        'Ã‰': 'É',
        'Ã': 'í', # Backup para 'início' quando o 'i' é engolido
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Casos específicos vistos no print
    content = content.replace('mÃ©todo', 'método')
    content = content.replace('nÃ£o', 'não')
    content = content.replace('vocÃª', 'você')
    content = content.replace('experiÃªncia', 'experiência')
    content = content.replace('disposiÃ§Ã£o', 'disposição')
    content = content.replace('inÃ­cio', 'início')
    content = content.replace('mÃºsicas', 'músicas')
    content = content.replace('jÃ¡', 'já')
    content = content.replace('enrolaÃ§Ã£o', 'enrolação')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_encoding('index.html')
    print("Correção de caracteres concluída!")
