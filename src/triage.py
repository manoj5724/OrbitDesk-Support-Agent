class Triage:

    def classify(self, question):

        question = question.lower()

        if "refund" in question or "legal" in question:
            return "out_of_scope"

        if "not working" in question or "broken" in question:
            return "requires_clarification"

        return "answerable"