Program Description:

Instantiate objects based on different budget categories like food, clothing, and entertainment.
When objects are created, they are passed in the name of the category.
The class will have an instance variable called ledger that is a list.

The class will also contain the following methods:
    1. A deposit method that accepts an amount and description.
       If no description is given, it will default to an empty string.
       The method should append an object to the ledger list in the form of:
       {"amount": amount, "description": description}

    2. A withdraw method that is similar to the deposit method, but the amount passed in will be stored
       in the ledger as a negative number.
       If there are not enough funds, nothing will be added to the ledger.
       This method will return True if the withdrawal took place, and False otherwise.

    3. A get_balance method that returns the current balance of the budget category based on the deposits
       and withdrawals that have occurred.

    4. A transfer method that accepts an amount and another budget category as arguments.
       The method will add a withdrawal with the amount and the description:
       "Transfer to [Destination Budget Category]"
       The method will then add a deposit to the other budget category with the amount and the description:
       "Transfer from [Source Budget Category]"
       If there are not enough funds, nothing will be added to either ledgers.
       This method will return True if the transfer took place, and False otherwise.

    5. A check_funds method that accepts an amount as an argument.
       It returns False if the amount is greater than the balance of the budget category and returns
       True otherwise.
       This method will be used by both the withdraw method and transfer method.

When the budget object is printed it will display:
    1. A title line of 30 characters where the name of the category is centered in a line of * characters.

    2. A list of the items in the ledger.
       Each line will show the description and amount.
       The first 23 characters of the description will be displayed, then the amount.
       The amount will be right aligned, contain two decimal places, and display a maximum of 7 characters.

    3. A line displaying the category total.


Here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96


Besides the Category class, the program has a function (outside of the class) called create_spend_chart
that takes a list of categories as an argument and returns a string that is a bar chart.
The chart will show the percentage spent in each category passed in to the function.
The percentage spent will be calculated only with withdrawals and not with deposits.
Down the left side of the chart will be labels 0 - 100.
The "bars" in the bar chart will be made out of the "o" character.
The height of each bar will be rounded down to the nearest 10.
The horizontal line below the bars will go two spaces past the final bar.
Each category name will be written vertically below the bar.
There will be a title at the top that says:
"Percentage spent by category"


Here is an example of the output:

Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g


The file test_module.py is a unit test.
