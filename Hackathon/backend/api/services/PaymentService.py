from abc import ABC, abstractmethod


class PaymentFactory(ABC):
    @abstractmethod
    def create_net_banking_payment(self):
        pass

    @abstractmethod
    def create_credit_card_payment(self):
        pass

    @abstractmethod
    def create_upi_payment(self):
        pass


class CreditCardPayment(ABC):
    @abstractmethod
    def process_credit_card_payment(self, amount: float) -> None:
        pass


class NetBankingPayment(ABC):
    @abstractmethod
    def process_net_banking_payment(self, amount: float) -> None:
        pass


class UPIPayment(ABC):
    @abstractmethod
    def process_upi_payment(self, amount: float) -> None:
        pass


class PhonePeNetBankingPayment(NetBankingPayment):
    def process_net_banking_payment(self, amount: float) -> None:
        print("Using PhonePe net banking payment")


class PhonePeCreditCardPayment(CreditCardPayment):
    def process_credit_card_payment(self, amount: float) -> None:
        print("Using PhonePe credit card payment")


class PhonePeUPIPayment(UPIPayment):
    def process_upi_payment(self, amount: float) -> None:
        print("Using PhonePe upi payment")


class PhonePePaymentFactory(PaymentFactory):

    def create_net_banking_payment(self):
        return PhonePeNetBankingPayment()

    def create_credit_card_payment(self):
        return PhonePeCreditCardPayment()

    def create_upi_payment(self):
        return PhonePeUPIPayment()
    


class RazorPayNetBankingPayment(NetBankingPayment):
    def process_net_banking_payment(self, amount: float) -> None:
        print("Using RazorPay net banking payment")


class RazorPayCreditCardPayment(CreditCardPayment):
    def process_credit_card_payment(self, amount: float) -> None:
        print("Using RazorPay credit card payment")


class RazorPayUPIPayment(UPIPayment):
    def process_upi_payment(self, amount: float) -> None:
        print("Using RazorPay upi payment")


class RazorPayPaymentFactory(PaymentFactory):

    def create_net_banking_payment(self):
        return RazorPayNetBankingPayment()

    def create_credit_card_payment(self):
        return RazorPayCreditCardPayment()

    def create_upi_payment(self):
        return RazorPayUPIPayment()
    


# Separate health checkers for each payment system
class PaymentGatewayHealthCheckerInterface:
    @abstractmethod
    def check_health(self):
        pass

class RazorPayHealthChecker(PaymentGatewayHealthCheckerInterface):
    def check_health(self):
        # Actual health check for RazorPay
        return False  

class PhonePeHealthChecker(PaymentGatewayHealthCheckerInterface):
    def check_health(self):
        # Actual health check for PhonePe
        return True

# Observer Pattern's main Observable class
class PaymentGatewayHealthChecker:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentGatewayHealthChecker, cls).__new__(cls)
            cls._instance._observers = []
            cls._instance._default_payment = "razor_pay"
            cls._instance._health_checkers = {
                "razor_pay": RazorPayHealthChecker(),
                "phone_pe": PhonePeHealthChecker(),
            }
        return cls._instance
    
    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._default_payment)

    def check_health(self):
        current_checker = self._health_checkers.get(self._default_payment)
        
        if not current_checker.check_health():
            for payment_method, checker in self._health_checkers.items():
                if checker.check_health():
                    self._default_payment = payment_method
                    self.notify_observers()
                    break


class PaymentManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentManager, cls).__new__(cls)
            cls._instance.payment_solution = None
        return cls._instance

    def reset_payment_solution(self, payment_provider):
        factories = {
            "razor_pay": RazorPayPaymentFactory(),
            "phone_pe": PhonePePaymentFactory(),
        }
        self.payment_solution = factories.get(payment_provider)
        if not self.payment_solution:
            print("Unknown payment provider. Cannot reset.")
            return

        self.credit_card_payment = self.payment_solution.create_credit_card_payment()
        self.net_banking = self.payment_solution.create_net_banking_payment()
        self.upi_payment = self.payment_solution.create_upi_payment()

    def update(self, default_payment):
        self.reset_payment_solution(default_payment)

    def process_payment_with_net_banking(self, amount):
        self.net_banking.process_net_banking_payment(amount)

    def process_payment_with_credit_card(self, amount):
        self.credit_card_payment.process_credit_card_payment(amount)

    def process_payment_with_upi(self, amount):
        self.upi_payment.process_upi_payment(amount)


class PaymentServiceImp:
    def __init__(self) -> None:
        # Health checker and payment manager setup
        self.health_checker = PaymentGatewayHealthChecker()
        self.payment_manager = PaymentManager()

        # Registering payment manager as an observer
        self.health_checker.register_observer(self.payment_manager)
    
    def _check_and_update_payment_solution(self):
        # Performing health check
        self.health_checker.check_health()

    def initiate_payment(self, amount, method):
        self._check_and_update_payment_solution()

        payment_id = str(uuid.uuid4())
        if method == "credit_card":
            self.payment_manager.process_payment_with_credit_card(amount)
        elif method == "net_banking":
            self.payment_manager.process_payment_with_net_banking(amount)
        elif method == "upi":
            self.payment_manager.process_payment_with_upi(amount)