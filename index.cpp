#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;

public:
    BankAccount(const string& accNumber, const string& accHolder) {
        accountNumber = accNumber;
        accountHolder = accHolder;
        balance = 0.0;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Amount " << amount << " deposited successfully." << endl;
        }
        else {
            cout << "Invalid amount. Deposit failed." << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Amount " << amount << " withdrawn successfully." << endl;
        }
        else {
            cout << "Insufficient funds or invalid amount. Withdrawal failed." << endl;
        }
    }

    void checkBalance() {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Account Number: " << accountNumber << endl;
        cout << "Current Balance: " << balance << endl;
    }
};

int main() {
    BankAccount myAccount("123456789", "John Doe");

    myAccount.checkBalance();
    myAccount.deposit(500);
    myAccount.withdraw(200);
    myAccount.checkBalance();

    return 0;
}

