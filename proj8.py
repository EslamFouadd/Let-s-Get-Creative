# Complex numbers

class ComplexNumber:
    """
    Represents a complex number.
    """

    def __init__(self, real, imaginary):
        """
        Initializes a complex number with the given real and imaginary parts.
        
        Parameters:
            real (float): The real part of the complex number.
            imaginary (float): The imaginary part of the complex number.
        """
        self.real = real
        self.imaginary = imaginary

    def conjugate(self):
        """
        Computes the conjugate of the complex number.
        
        Returns:
            ComplexNumber: The conjugate of the complex number.
        """
        return ComplexNumber(self.real, -self.imaginary)

    def modulus(self):
        """
        Computes the modulus (absolute value) of the complex number.
        
        Returns:
            float: The modulus of the complex number.
        """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __add__(self, other):
        """
        Adds two complex numbers.
        
        Parameters:
            other (ComplexNumber): The complex number to add.
        
        Returns:
            ComplexNumber: The result of adding the two complex numbers.
        """
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        """
        Subtracts two complex numbers.
        
        Parameters:
            other (ComplexNumber): The complex number to subtract.
        
        Returns:
            ComplexNumber: The result of subtracting the two complex numbers.
        """
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        """
        Multiplies two complex numbers.
        
        Parameters:
            other (ComplexNumber): The complex number to multiply.
        
        Returns:
            ComplexNumber: The result of multiplying the two complex numbers.
        """
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        """
        Divides two complex numbers.
        
        Parameters:
            other (ComplexNumber): The complex number to divide by.
        
        Returns:
            ComplexNumber: The result of dividing the two complex numbers.
        """
        conjugate_other = other.conjugate()
        denominator = other * conjugate_other
        numerator = self * conjugate_other
        real_part = numerator.real / denominator.real
        imaginary_part = numerator.imaginary / denominator.real
        return ComplexNumber(real_part, imaginary_part)

    # Other methods such as __eq__, __ne__, etc. can be added as needed.

# Example
# Create and manipulate complex numbers
z1 = ComplexNumber(3, 4)  # 3 + 4i
z2 = ComplexNumber(1, -2) # 1 - 2i

# Addition
result_addition = z1 + z2
print("Addition:", result_addition)  # Output: (4 + 2i)

# Subtraction
result_subtraction = z1 - z2
print("Subtraction:", result_subtraction)  # Output: (2 + 6i)

# Multiplication
result_multiplication = z1 * z2
print("Multiplication:", result_multiplication)  # Output: (11 + 2i)

# Division
result_division = z1 / z2
print("Division:", result_division)  # Output: (1.8 + 2.2i)