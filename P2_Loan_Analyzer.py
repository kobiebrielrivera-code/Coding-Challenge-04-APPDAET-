def validate_loan_inputs(principal, annual_rate, months, extra_payment=0, rate_shock=0):
    if principal <= 0:
        raise ValueError("Principal must be positive.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if months <= 0 or not isinstance(months, int):
        raise ValueError("Term (months) must be a positive integer.")
    if extra_payment < 0:
        raise ValueError("Extra payment cannot be negative.")
    if rate_shock < 0:
        raise ValueError("Rate shock cannot be negative.")
    return True


def calculate_monthly_payment(principal, annual_rate, months):
    r = annual_rate / 12 / 100
    if r == 0:
        return principal / months
    return principal * r * (1 + r) ** months / ((1 + r) ** months - 1)


def calculate_monthly_interest(balance, annual_rate):
    r = annual_rate / 12 / 100
    return balance * r


def simulate_payoff_months(principal, annual_rate, months, extra_payment=0):
    balance = principal
    payment = calculate_monthly_payment(principal, annual_rate, months)
    count = 0
    while balance > 1e-8:
        interest = calculate_monthly_interest(balance, annual_rate)
        total_payment = payment + extra_payment
        principal_portion = total_payment - interest
        if principal_portion > balance:
            principal_portion = balance
        balance -= principal_portion
        count += 1
        if count > 100000:
            break
    return count


def simulate_total_interest(principal, annual_rate, months, extra_payment=0):
    balance = principal
    payment = calculate_monthly_payment(principal, annual_rate, months)
    total_interest = 0
    count = 0
    while balance > 1e-8:
        interest = calculate_monthly_interest(balance, annual_rate)
        total_payment = payment + extra_payment
        principal_portion = total_payment - interest
        if principal_portion > balance:
            principal_portion = balance
        total_interest += interest
        balance -= principal_portion
        count += 1
        if count > 100000:
            break
    return total_interest


def calculate_stressed_payment(principal, annual_rate, months, rate_shock):
    stressed_rate = annual_rate + rate_shock
    return calculate_monthly_payment(principal, stressed_rate, months)


def calculate_savings(baseline_months, baseline_interest, accelerated_months, accelerated_interest):
    months_saved = baseline_months - accelerated_months
    interest_saved = baseline_interest - accelerated_interest
    return months_saved, interest_saved


def generate_summary(principal, annual_rate, months, extra_payment, rate_shock):
    validate_loan_inputs(principal, annual_rate, months, extra_payment, rate_shock)

    regular_payment = calculate_monthly_payment(principal, annual_rate, months)
    baseline_interest = simulate_total_interest(principal, annual_rate, months, 0)

    accelerated_months = simulate_payoff_months(principal, annual_rate, months, extra_payment)
    accelerated_interest = simulate_total_interest(principal, annual_rate, months, extra_payment)

    months_saved, interest_saved = calculate_savings(
        months, baseline_interest, accelerated_months, accelerated_interest
    )

    stressed_payment = calculate_stressed_payment(principal, annual_rate, months, rate_shock)

    print(f"Regular monthly payment: PHP {regular_payment:,.2f}")
    print(f"Baseline total interest: PHP {baseline_interest:,.2f}")
    print(f"Accelerated payoff: {accelerated_months} months")
    print(f"Accelerated total interest: PHP {accelerated_interest:,.2f}")
    print(f"Months saved: {months_saved}")
    print(f"Interest saved: PHP {interest_saved:,.2f}")
    print(f"Stressed payment (+{rate_shock}%): PHP {stressed_payment:,.2f}")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("=== Loan Repayment, Extra-Payment, and Rate-Stress Analyzer ===")
    principal = get_float_input("Enter loan principal: ")
    annual_rate = get_float_input("Enter annual interest rate (%): ")
    months = get_int_input("Enter loan term (months): ")
    extra_payment = get_float_input("Enter extra monthly payment (0 if none): ")
    rate_shock = get_float_input("Enter rate shock for stress test (percentage points): ")

    try:
        generate_summary(principal, annual_rate, months, extra_payment, rate_shock)
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()