from typing import Annotated

from semantic_kernel.functions.kernel_function_decorator import kernel_function


class MathPlugin:
    """Description: MathPlugin provides a set of functions to make Math calculations.

    Usage:
        kernel.add_plugin(MathPlugin(), plugin_name="math")

    Examples:
        {{math.Add}} => Returns the sum of input and amount (provided in the KernelArguments)
        {{math.Subtract}} => Returns the difference of input and amount (provided in the KernelArguments)
        {{math.Multiply}} => Returns the muliplication of first and second number (provided in the KernelArguments))
    """

    @kernel_function(name="Add", description="Returns the Addition result of the values provided.")
    def add(
        self,
        input: Annotated[int, "the first number to add"],
        amount: Annotated[int, "the second number to add"],
    ) -> Annotated[int, "the output is a number"]:
        """Returns the Addition result of the values provided."""
        if isinstance(input, str):
            input = int(input)
        if isinstance(amount, str):
            amount = int(amount)
        return MathPlugin.add_or_subtract(input, amount, add=True)

    @kernel_function(name="Subtract", description="Returns the difference of numbers provided.")
    def subtract(
        self,
        input: Annotated[int, "the first number"],
        amount: Annotated[int, "the number to subtract"],
    ) -> int:
        """Returns the difference of numbers provided."""
        if isinstance(input, str):
            input = int(input)
        if isinstance(amount, str):
            amount = int(amount)
        return MathPlugin.add_or_subtract(input, amount, add=False)
    
    @kernel_function(name="Multiply", description="Multiply the first number by the second number.")
    def multiply(
        self, 
        first: Annotated[int, "the first number to multiply"],
        second: Annotated[int, "the second number to multiply"],
    ) -> int:
        """Multiply the first number by the second number."""
        if isinstance(first, str):
            first = int(first)
        if isinstance(second, str):
            second = int(second)
        return first * second
    
    @kernel_function(name="Divid", description="Divid the first number by the second number.")
    def divid(
        self, 
        first: Annotated[float, "the first number, dividend"],
        second: Annotated[float, "the second number, divisor"],
    ) -> int:
        """ the first number by the second number."""
        if isinstance(first, str):
            first = float(first)
        if isinstance(second, str):
            second = float(second)
        return first / second

    @staticmethod
    def add_or_subtract(input: int, amount: int, add: bool) -> int:
        """Helper function to perform addition or subtraction based on the add flag."""
        return input + amount if add else input - amount