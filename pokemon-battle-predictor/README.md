```markdown
# Pokémon Battle Prediction

This project predicts the **win probability** of Pokémon battles based on their stats and type matchups.  
Users can select a team of Pokémon, choose a fighter, and see a **ranked probability of winning** against a random opponent.

---

## Dataset

* Source: Custom Pokémon stats dataset (CSV) with the following columns:

  * **Name** – Pokémon name  
  * **Type 1**, **Type 2** – Primary and secondary types  
  * **HP, Attack, Defense, Sp. Atk, Sp. Def, Speed** – Base stats  
  * **Total** – Sum of all stats  
  * **Generation** – Pokémon generation  
  * **Legendary** – Boolean flag if Pokémon is legendary  

* Example entry:
```

Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False

```

* Missing Type 2 values were replaced with `"None"` for consistency.

---

## Win Probability Prediction

The project uses **Logistic Regression** to predict the probability of a Pokémon winning a battle.

### Steps:

1. **Feature Engineering:**  
   - Stat differences (`Attack vs Defense`, `Speed difference`)  
   - Type effectiveness scores  
   - Total stats  

2. **Model Training:**  
   - Train-test split (80%-20%)  
   - Logistic Regression from `scikit-learn`  

3. **Evaluation:**  
   - Accuracy: ~93-94%  
   - Confusion matrix and classification report  

4. **Battle Simulation:**  
   - Users pick 5 Pokémon  
   - Random opponent is selected  
   - Users choose a fighter  
   - Model outputs **probabilities for all team members**  
   - Ranked probabilities indicate the best choice  

---

## Example Output

```

Opponent Pokémon: Jellicent
Chosen Pokémon: Charmander
That’s a really bad matchup.

\---------- Battle Results ----------

1. Bulbasaur: 98.34%  → ✅ Excellent pick
2. Pikachu: 42.51%    → 🤔 Risky pick
3. Butterfree: 2.01%  → ❌ Bad pick
4. Rattata: 0.01%     → ❌ Bad pick
5. Charmander: 0.00%  → ❌ Bad pick

Comparing stats: Charmander vs Jellicent

````

---

## Visualizations (Plotly)

* Interactive **radar chart** comparing stats of the opponent vs chosen Pokémon  
* Users can see **HP, Attack, Defense, Sp. Atk, Sp. Def, Speed** in a single chart

---

## Files in Repo

* `data/pokemon_stats.csv` – Pokémon stats dataset  
* `notebooks/main.ipynb` – Code for training model, simulating battles, and visualizations  
* `results/` – Battle probability outputs  
* `README.md` – Project documentation  

---

## Tools & Libraries Used

* Python  
* Pandas, NumPy  
* Scikit-learn (Logistic Regression)  
* Plotly (Radar chart visualizations)  
* Random (for opponent selection)  

---

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/pokemon-battle-predictor.git
cd pokemon-battle-predictor
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open Jupyter Notebook and run `main.ipynb`.

---

## License

This project is licensed under the MIT License.

```

---

```
