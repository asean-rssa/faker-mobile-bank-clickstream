events = [
    "Login",
    "Logout",
    "ViewHome",
    "ViewAccounts",
    "ViewProducts",
    "SelectTransfer",
    "ViewTransactions",
    "ViewCreditCard",
    "ViewLoan",
    "ApplyCreditCard",
    "ApplyLoan",
    "FillCreditCardApplication",
    "FillLoanApplication",
    "SubmitCreditCardApplication",
    "SubmitLoanApplication",
    "FillTransferDetails",
    "CompleteTransfer"
]

weighted_events = [
    {
        "name": "Login",
        "popularity": 0,
        "dependsOn": [] 
    },
    {
        "name": "Logout",
        "popularity": 2,
        "dependsOn": ["Login"] 
    },
    {
        "name": "ViewHome",
        "popularity": 10,
        "dependsOn": ["Login"] 
    },
    {
        "name": "ViewAccounts",
        "popularity": 10,
        "dependsOn": ["Login"] 
    },
    {
        "name": "ViewProducts",
        "popularity": 10,
        "dependsOn": ["Login"] 
    },
    {
        "name": "SelectTransfer",
        "popularity": 20,
        "dependsOn": ["Login"] 
    },
    {
        "name": "ViewTransactions",
        "popularity": 60,
        "dependsOn": ["ViewAccounts"] 
    },
    {
        "name": "ViewCreditCard",
        "popularity": 40,
        "dependsOn": ["ViewProducts"] 
    },
    {
        "name": "ViewLoan",
        "popularity": 40,
        "dependsOn": ["ViewProducts"] 
    },
    {
        "name": "ApplyCreditCard",
        "popularity": 60,
        "dependsOn": ["ViewProducts"] 
    },
    {
        "name": "ApplyLoan",
        "popularity": 60,
        "dependsOn": ["ViewProducts"] 
    },
    {
        "name": "FillCreditCardApplication",
        "popularity": 80,
        "dependsOn": ["ApplyCreditCard"] 
    },
    {
        "name": "FillLoanApplication",
        "popularity": 80,
        "dependsOn": ["ApplyLoan"] 
    },
    {
        "name": "SubmitCreditCardApplication",
        "popularity": 100,
        "dependsOn": ["ApplyCreditCard"] 
    },
    {
        "name": "SubmitLoanApplication",
        "popularity": 100,
        "dependsOn": ["ApplyLoan"] 
    },
    {
        "name": "FillTransferDetails",
        "popularity": 80,
        "dependsOn": ["SelectTransfer"] 
    },
    {
        "name": "CompleteTransfer",
        "popularity": 100,
        "dependsOn": ["FillTransferDetails"] 
    }
]