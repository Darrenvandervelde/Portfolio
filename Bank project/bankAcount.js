class bankAccount {
    constructor(accountNumber, accountHolder, balance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;

        this.deposit = function (inputMoney) {
            balance = balance + inputMoney;
        }

        this.withdraw = function (exitMoney) {
            balance = balance - exitMoney;
        }

        this.checkBalance = function () {
            alert("Your balance is: " + balance + ".");
            return balance;
        }
    }
}