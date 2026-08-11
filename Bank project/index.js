class bankAccount {
    constructor(accountNumber, accountHolder, balance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    deposit(inputMoney) {
        this.balance = this.balance + Number(inputMoney);
    }

    withdraw(exitMoney) {
        this.balance = this.balance - Number(exitMoney);
    }

    checkBalance() {

        alert("Your balance is: " + this.balance + ".");
    }
}

const user = new bankAccount(224, "Mr Harry Theokli", 2220);

function printBalance() {

}