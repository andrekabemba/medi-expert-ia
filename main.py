from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import uvicorn

# IMPORTATION DU FICHIER DES RÈGLES
import regles

app = FastAPI(title="MediExpert System")
templates = Jinja2Templates(directory="templates")

class ExpertSystem:
    """Moteur d'inférence amélioré avec système de score."""
    
    @staticmethod
    def diagnose(user_symptoms: List[str]) -> List[dict]:
        results = []
        user_symptoms_set = set(user_symptoms)
        
        for disease in regles.DISEASES:
            disease_symptoms = set(disease["symptoms"])
            
            # Calcul de l'intersection (symptômes communs)
            matches = disease_symptoms.intersection(user_symptoms_set)
            match_count = len(matches)
            total_required = len(disease_symptoms)
            
            # Calcul du score de confiance en pourcentage
            confidence = int((match_count / total_required) * 100)
            
            # On ne retient que les maladies qui ont au moins un symptôme en commun
            if confidence > 0:
                # On crée une copie pour ajouter le score sans modifier l'original
                result = disease.copy()
                result["confidence"] = confidence
                result["matched_symptoms"] = list(matches)
                results.append(result)
        
        # Tri des résultats par score de confiance décroissant
        return sorted(results, key=lambda x: x["confidence"], reverse=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"symptoms": regles.ALL_SYMPTOMS}
    )

@app.post("/diagnose")
async def diagnose(selected_symptoms: Optional[List[str]] = Form(None)):
    if not selected_symptoms:
        return {"results": []}
    
    # Appel du moteur d'inférence flexible
    results = ExpertSystem.diagnose(selected_symptoms)
    
    # Debug console pour voir les probabilités
    print(f"Symptômes sélectionnés : {selected_symptoms}")
    for r in results:
        print(f" - {r['name']} : {r['confidence']}%")
        
    return {"results": results}

if __name__ == "__main__":
    # 127.0.0.1 pour avoir un lien cliquable dans la console
    uvicorn.run(app, host="127.0.0.1", port=8000)
