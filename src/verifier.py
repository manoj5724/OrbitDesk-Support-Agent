class Verifier:

    def verify(self, output):

        # Answer empty hai ya nahi
        if not output["answer"].strip():
            output["classification"] = "safe_failure"
            output["reason"] = "Answer generation failed."
            return output

        # Source mila ya nahi
        if len(output["sources"]) == 0:
            output["classification"] = "safe_failure"
            output["reason"] = "No supporting source found."
            return output

        # Confidence check
        if output["confidence"] < 0.5:
            output["requires_human"] = True

        return output