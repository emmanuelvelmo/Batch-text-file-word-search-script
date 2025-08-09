#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <regex>
#include <algorithm>
#include <cctype>

int main()
{
    // Bucle principal continuo
    while (true)
    {
        // Directorio de entrada
        std::string directorio_val;
        while (true)
        {
            std::cout << "Enter directory: ";
            std::getline(std::cin, directorio_val);
            
            // Remover comillas si las hay
            if (directorio_val.front() == '"' || directorio_val.front() == '\'')
                directorio_val = directorio_val.substr(1);

            if (directorio_val.back() == '"' || directorio_val.back() == '\'')
                directorio_val.pop_back();
            
            if (std::filesystem::is_directory(directorio_val))
                break;

            std::cout << "Wrong directory\n";
        }
        
        std::string palabra_val;

        std::cout << "Enter text to search: ";
        std::getline(std::cin, palabra_val);

        std::cout << "------------------------------------\n";
        
        // Búsqueda insensible a mayúsculas/minúsculas usando regex
        std::string patron_str = "\\b" + palabra_val + "\\b";
        
        std::regex patron_busqueda(patron_str, std::regex_constants::icase);
        
        // Buscar en todos los archivos del directorio recursivamente
        for (const std::filesystem::directory_entry &entrada : std::filesystem::recursive_directory_iterator(directorio_val))
        {
            if (entrada.is_regular_file())
            {
                std::string ruta_completa = entrada.path().string();
                
                // Probar diferentes codificaciones (simulado con manejo de excepciones)
                try
                {
                    std::ifstream arch(ruta_completa);
                    
                    if (arch)
                    {
                        std::string contenido_val((std::istreambuf_iterator<char>(arch)), std::istreambuf_iterator<char>());
                        
                        if (std::regex_search(contenido_val, patron_busqueda))
                        {
                            std::cout << ruta_completa << "\n";
                        }
                    }
                }
                catch (const std::exception &e)
                {
                    // Si ocurre un error al abrir o leer el archivo, simplemente lo ignoramos
                    continue;
                }
            }
        }
        
        std::cout << "------------------------------------\n\n";
    }
    
    return 0;
}
