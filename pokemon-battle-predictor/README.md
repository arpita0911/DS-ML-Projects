---

# Pokémon Battle Prediction

This project predicts the win probability of Pokémon battles based on their stats and type matchups.
Users can select a team of Pokémon, choose a fighter, and see a ranked probability of winning against a random opponent.

---

## Dataset

* Source: [Pokémon Stats (English)](https://www.kaggle.com/datasets/abcsds/pokemon) from Kaggle
* Columns:
  * Name – Pokémon name
  * Type 1, Type 2 – Primary and secondary types
  * HP, Attack, Defense, Sp. Atk, Sp. Def, Speed – Base stats
  * Total – Sum of all stats
  * Generation – Pokémon generation
  * Legendary – Boolean flag if Pokémon is legendary
---

## Win Probability Prediction

The project uses Logistic Regression to predict the probability of a Pokémon winning a battle.

Steps:

1. Feature Engineering:

   * Stat differences (Attack vs Defense)
   * Type effectiveness scores
   * Speed Bonus
   * Total stats

2. Model Training:

   * Train-test split (80%-20%)
   * Logistic Regression from scikit-learn

3. Evaluation:

   * Accuracy: \~93-94%
   * Confusion matrix and classification report

4. Battle Simulation:

   * Users pick 5 Pokémon
   * Random opponent is selected
   * Users choose a fighter
   * Model outputs probabilities for all team members
   * Ranked probabilities indicate the best choice

---

### Example Output

Opponent Pokémon: Jellicent
Chosen Pokémon: Charmander
That’s a really bad matchup.

Battle Results:

1. Bulbasaur: 98.34% – Excellent pick
2. Pikachu: 42.51% – Risky pick
3. Butterfree: 2.01% – Bad pick
4. Rattata: 0.01% – Bad pick
5. Charmander: 0.00% – Bad pick

Comparing stats: Charmander vs Jellicent

---

## Visualizations

* Interactive radar chart comparing stats of the opponent vs chosen Pokémon
* Interactive bar chart showing win probabilities of team members against the selected opponent

---

## Files in Repo

* data/pokemon.csv – Pokémon stats dataset
* notebooks/main.ipynb – Code for training model, simulating battles, and visualizations
* README.md – Project documentation

---

## Tools and Libraries Used

* Python
* Pandas, NumPy
* Scikit-learn (Logistic Regression)
* Plotly (Visualizations)
* Random (for opponent selection)

---

## How to Run

1. Clone the repo:

git clone https://github.com/arpita0911/DS-ML-Projects.git

cd DS-ML-Projects/pokemon-battle-predictor

2. Install dependencies:

pip install -r requirements.txt

3. Open Jupyter Notebook and run main.ipynb

---
