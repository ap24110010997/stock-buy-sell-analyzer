## Stock Buy-Sell Analyzer

### Greedy & Dynamic Programming Approach

---

 ## Project Description

The **Stock Buy-Sell Analyzer** is a Python project that calculates the **maximum profit** from stock prices using:

*  Greedy Algorithm (efficient approach)
*  Dynamic Programming (optimal approach)

It also displays **buy/sell transactions** and compares both methods.

---

## Objectives

* Analyze stock price data
* Maximize profit using algorithms
* Compare Greedy vs Dynamic Programming
* Display clear buy/sell decisions

---

##  Technologies Used

* Python 3
* VS Code / Any IDE
* Git & GitHub

---

##  Project Structure

```
stock-buy-sell-analyzer/
│── main.py        # Main execution file
│── greedy.py      # Greedy algorithm logic
│── dp.py          # Dynamic Programming logic
│── utils.py       # Helper functions
│── README.md      # Documentation
```

---

##  Algorithms Used

###  Greedy Algorithm

* Buys and sells whenever there is a profit opportunity
* Works for unlimited transactions
* Fast and efficient

**Time Complexity:** O(n)

---

###  Dynamic Programming

* Checks all possible combinations
* Ensures optimal solution
* Useful for advanced constraints

**Time Complexity:** O(n²)

---

##  How to Run

### 1️ Clone the Repository

```bash
git clone https://github.com/your-username/stock-buy-sell-analyzer.git
cd stock-buy-sell-analyzer
```

### 2️ Run the Program

```bash
python main.py
```

### 3 Enter Input

```
Enter stock prices (space separated): 7 1 5 3 6 4
```

---

##  Sample Input

```
7 1 5 3 6 4
```

---

##  Sample Output

```
--- Results ---
Greedy Profit: 7
Buy on day 1 at price 1, Sell on day 2 at price 5
Buy on day 3 at price 3, Sell on day 4 at price 6

DP Profit: 7
```

---

##  Explanation

* The program detects profitable buy/sell points
* Greedy approach captures all increasing trends
* DP approach ensures maximum possible profit

---

##  Comparison

| Feature     | Greedy | DP      |
| ----------- | ------ | ------- |
| Speed       | Fast   | Slower  |
| Complexity  | O(n)   | O(n²)   |
| Accuracy    | Good   | Optimal |
| Flexibility | Low    | High    |

---

## Future Improvements

*  Graph visualization
*  Web interface
*  Live stock data
*  Transaction constraints
  
---
## TEAM MEMBERS:

* AP24110011006
* AP24110010997
* AP24110010982
* AP24110011034
* AP24110010936
