# 🐚 Custom Linux-like Shell (Python)

**Asignatura**: Sistemas Computacionales y Redes (2025)  
**Autor**: [Amalia González Ortega]  
**Fecha de entrega**: 20 de abril de 2025  

---

## 🎯 Objetivo
Implementar un shell minimalista en Python que emule las funcionalidades básicas de los shells de Linux (como `bash`), incluyendo manejo de comandos, redirecciones, pipes y procesos en background.

---

## ✅ Funcionalidades Implementadas

### 🔹 **Básicas**  
- Prompt personalizado (`$ `).  
- Ejecución de comandos externos (`ls`, `grep`, etc.).  
- Comando `cd` para cambiar de directorio.  
- Redirecciones:  
  - `>` (sobrescribir archivo),  
  - `>>` (añadir a archivo),  
  - `<` (entrada desde archivo).  
- Pipes (`|`) entre comandos.  

### 🔹 **Adicionales**  
- [✅] **Múltiples pipes** (`comando1 | comando2 | comando3`).  
- [✅] **Procesos en background** (`&`), `jobs` y `fg`.  
- [✅] **Espacios flexibles** entre comandos/operadores.  
- [✅] **Historial de comandos** (`history`, `!!`, `!n`, `!comando`).  
