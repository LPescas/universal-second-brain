#!/bin/bash
# ============================================================
# Second Brain — Full Setup Script (Bash/Linux/macOS)
# Creates complete structure, deploys integrations, configures CLI.
# Run: chmod +x setup.sh && ./setup.sh
# ============================================================

set -e

BRAIN_ROOT="$HOME/.second_brain"
PROJECTS_ROOT="$HOME/Projetos"  # Adjust as needed

echo ""
echo "============================================"
echo "  🧠 SECOND BRAIN — Setup Automático"
echo "============================================"
echo ""

# --- 1. Create structure ---
echo "[1/5] Criando estrutura de diretórios..."

dirs=(
    "$BRAIN_ROOT"
    "$BRAIN_ROOT/knowledge"
    "$BRAIN_ROOT/projects"
    "$BRAIN_ROOT/scripts"
    "$BRAIN_ROOT/integrations"
)

for dir in "${dirs[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "  ✅ Created: $dir"
    else
        echo "  ✔ Exists: $dir"
    fi
done

# --- 2. Verify core files ---
echo "[2/5] Verificando arquivos core..."

core_files=(
    "MASTER_INDEX.yaml"
    "global_rules.md"
    "behavioral_patterns.yaml"
    "learning_log.md"
)

for file in "${core_files[@]}"; do
    if [ -f "$BRAIN_ROOT/$file" ]; then
        echo "  ✔ $file"
    else
        echo "  ❌ MISSING: $file"
    fi
done

# --- 3. Deploy .cursorrules ---
echo "[3/5] Deploying .cursorrules..."

template="$BRAIN_ROOT/integrations/cursorrules_template.md"
if [ -f "$template" ] && [ -d "$PROJECTS_ROOT" ]; then
    for proj in "$PROJECTS_ROOT"/*/; do
        if [ -d "$proj" ]; then
            cp "$template" "$proj/.cursorrules"
            echo "  ✅ .cursorrules → $(basename $proj)"
        fi
    done
fi

# --- 4. Shell profile integration ---
echo "[4/5] Configurando shell profile..."

# Detect shell
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.bashrc"
fi

MARKER="# --- SECOND BRAIN INTEGRATION ---"

if grep -q "$MARKER" "$SHELL_RC" 2>/dev/null; then
    echo "  ✔ Second Brain already in $SHELL_RC"
else
    cat >> "$SHELL_RC" << 'ALIASES'

# --- SECOND BRAIN INTEGRATION ---
export SECOND_BRAIN="$HOME/.second_brain"

brain-learn() {
    local note="$*"
    local date=$(date '+%Y-%m-%d %H:%M')
    echo -e "\n### $date | USER | MANUAL\n- $note\n" >> "$SECOND_BRAIN/learning_log.md"
    echo "✅ Learning registered in Second Brain"
}

brain-index() { cat "$SECOND_BRAIN/MASTER_INDEX.yaml"; }
brain-sync() { bash "$SECOND_BRAIN/scripts/consolidate.sh"; }
brain-clean() { bash "$SECOND_BRAIN/scripts/cleanup.sh"; }

brain-project() {
    local path="$SECOND_BRAIN/projects/${1}_context.md"
    if [ -f "$path" ]; then
        cat "$path"
    else
        echo "❌ Project '$1' not found. Available:"
        ls "$SECOND_BRAIN/projects/"
    fi
}

brain-cursor() {
    cp "$SECOND_BRAIN/integrations/cursorrules_template.md" ./.cursorrules
    echo "✅ .cursorrules deployed to $(pwd)"
}

echo "🧠 Second Brain loaded. Commands: brain-learn, brain-index, brain-sync, brain-clean, brain-project, brain-cursor"
ALIASES

    echo "  ✅ Aliases injected into $SHELL_RC"
fi

# --- 5. Summary ---
echo ""
echo "[5/5] Escaneando projetos..."
if [ -d "$PROJECTS_ROOT" ]; then
    for proj in "$PROJECTS_ROOT"/*/; do
        name=$(basename "$proj" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
        ctx="$BRAIN_ROOT/projects/${name}_context.md"
        if [ -f "$ctx" ]; then
            echo "  ✔ $(basename $proj) → indexed"
        else
            echo "  ⚠️ $(basename $proj) → NOT INDEXED"
        fi
    done
fi

echo ""
echo "============================================"
echo "  ✅ SETUP COMPLETO!"
echo "============================================"
echo "  Hub: $BRAIN_ROOT"
echo "  Recarregue o terminal: source $SHELL_RC"
echo ""
