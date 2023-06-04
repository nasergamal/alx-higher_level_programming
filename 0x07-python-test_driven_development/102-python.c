#include <stdio.h>
#include "Python.h"

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{       printf("  [ERROR] Invalid String Object\n");
		return; }
	if PyUnicode_IS_COMPACT_ASCII((PyASCIIObject *)p)
		printf("  type: compact ascii\n");
	else if (PyUnicode_IS_COMPACT((PyASCIIObject *)p))
		printf("  type: compact unicode object\n");
	else
		printf("  type: compact ascii\n");
	printf("  length: %d\n", (int)((PyASCIIObject *)p)->length);

	printf("  value: ");
	PyObject_Print(p, stdout, 1);
	printf("\n");
}
