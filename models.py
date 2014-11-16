class Customer:
    def charge(self, amount, description):
        response = stripe.Charge.create(
            amount=100 * amount,
            customer=self.id,
            description=description,
        )
        log = self.record_charge(response['id'])
        return log
