#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - print python list info.
 * @p: python list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *ob;

	printf("[*] Size of the Python List =%d\n", (int)Py_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < (int)Py_SIZE(p); i++)
	{
		ob = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(ob)->tp_name);
	}
}
