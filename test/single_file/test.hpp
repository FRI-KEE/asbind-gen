#define ANNOTATED_FUNC [[clang::annotate("asbind:func")]]

ANNOTATED_FUNC
int f1();

float f2(float);

ANNOTATED_FUNC
int f3(int a, float b);

