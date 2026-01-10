
# Create the mermaid flowchart for Consciousness Trilogy project structure

diagram_code = """
flowchart TD
    Main["Consciousness Trilogy"]
    
    %% Main Categories
    CoreCat["Core Code"]
    DocCat["Documentation"]
    SuppCat["Support Files"]
    
    %% Core Code Files
    Core1["consciousness.py<br/>(Core Module)"]
    Core2["test_consciousness.py"]
    Core3["advanced_tests.py"]
    Core4["run_tests.py<br/>(Test Orchestrator)"]
    
    %% Documentation Files
    Doc1["README.md"]
    Doc2["PHILOSOPHY.md"]
    Doc3["CONTRIBUTING.md"]
    Doc4["LICENSE"]
    Doc5["PROJECT_SUMMARY.md"]
    Doc6["FILE_MANIFEST.md"]
    
    %% Support Files
    Supp1["examples.py"]
    Supp2["pyproject.toml"]
    Supp3[".gitignore"]
    
    %% Structure connections
    Main --> CoreCat
    Main --> DocCat
    Main --> SuppCat
    
    CoreCat --> Core1
    CoreCat --> Core2
    CoreCat --> Core3
    CoreCat --> Core4
    
    DocCat --> Doc1
    DocCat --> Doc2
    DocCat --> Doc3
    DocCat --> Doc4
    DocCat --> Doc5
    DocCat --> Doc6
    
    SuppCat --> Supp1
    SuppCat --> Supp2
    SuppCat --> Supp3
    
    %% Execution Flow (dependencies)
    Core1 -.->|used by| Core2
    Core1 -.->|used by| Core3
    Core2 -.->|orchestrated by| Core4
    Core3 -.->|orchestrated by| Core4
    Core1 -.->|used by| Supp1
    
    %% Styling
    classDef coreStyle fill:#B3D9FF,stroke:#1E90FF,stroke-width:2px,color:#000
    classDef docStyle fill:#C8E6C9,stroke:#4CAF50,stroke-width:2px,color:#000
    classDef suppStyle fill:#FFE0B2,stroke:#FF9800,stroke-width:2px,color:#000
    classDef catStyle fill:#F5F5F5,stroke:#666,stroke-width:2px,color:#000
    classDef mainStyle fill:#E8E8E8,stroke:#333,stroke-width:3px,color:#000
    
    class Main mainStyle
    class CoreCat,DocCat,SuppCat catStyle
    class Core1,Core2,Core3,Core4 coreStyle
    class Doc1,Doc2,Doc3,Doc4,Doc5,Doc6 docStyle
    class Supp1,Supp2,Supp3 suppStyle
"""

# Create the diagram using the helper function
create_mermaid_diagram(diagram_code, 'consciousness_trilogy_flowchart.png', 'consciousness_trilogy_flowchart.svg', width=1400, height=1000)
