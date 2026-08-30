# Interrompe a execução caso ocorra algum erro
$ErrorActionPreference = "Stop"

Write-Host "Iniciando a criação da estrutura do projeto..." -ForegroundColor Cyan

# 1. Criação da árvore de diretórios
$pastas = @(
    "backend/app/api/v1/endpoints",
    "backend/app/core",
    "backend/app/models",
    "backend/app/schemas",
    "frontend/src/components",
    "frontend/src/layouts",
    "frontend/src/pages",
    "frontend/src/services",
    "frontend/src/types"
)

foreach ($pasta in $pastas) {
    if (-not (Test-Path $pasta)) {
        New-Item -ItemType Directory -Path $pasta | Out-Null
        Write-Host "Criado diretório: $pasta" -ForegroundColor Green
    } else {
        Write-Host "Diretório já existe: $pasta" -ForegroundColor Yellow
    }
}

# 2. Criação dos arquivos base vazios ou com estrutura inicial essencial
$arquivos = @(
    # Raiz
    "docker-compose.yml",
    
    # Back-end
    "backend/requirements.txt",
    "backend/Dockerfile",
    "backend/app/main.py",
    "backend/app/core/__init__.py",
    "backend/app/core/database.py",
    "backend/app/core/config.py",
    "backend/app/models/__init__.py",
    "backend/app/schemas/__init__.py",
    "backend/app/api/__init__.py",
    "backend/app/api/v1/__init__.py",
    "backend/app/api/v1/router.py",
    "backend/app/api/v1/endpoints/__init__.py",
    "backend/app/api/v1/endpoints/iniciacao.py",
    "backend/app/api/v1/endpoints/modelagem.py",
    "backend/app/api/v1/endpoints/execucao.py",
    "backend/app/api/v1/endpoints/encerramento.py",

    # Front-end
    "frontend/package.json",
    "frontend/tsconfig.json",
    "frontend/src/main.tsx",
    "frontend/src/App.tsx"
)

foreach ($arquivo in $arquivos) {
    if (-not (Test-Path $arquivo)) {
        New-Item -ItemType File -Path $arquivo | Out-Null
        Write-Host "Criado arquivo: $arquivo" -ForegroundColor DarkGreen
    } else {
        Write-Host "Arquivo já existe: $arquivo" -ForegroundColor Yellow
    }
}

Write-Host "Estrutura do projeto criada com sucesso!" -ForegroundColor Cyan