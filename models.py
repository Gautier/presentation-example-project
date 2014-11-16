class Customer:
    def charge(self, amount, description, currency):
        response = stripe.Charge.create(
            amount=100 * amount,
            currency=curency,
            customer=self.id,
            description=description,
        )
        log = self.record_charge(response['id'])
        return log
