#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int verified = 0;
    char user_key[10];

    /* Read user's credentials. */

    printf("Enter password: ");
    if (fgets(user_key, sizeof(user_key), stdin) != NULL)
    {
        size_t len = strlen(user_key);
        if (len > 0 && user_key[len-1] == '\n') {
            user_key[len-1] = '\0';  // Remove newline character
        }
    }

    /* Verify credentials. */

    if (!strcmp(user_key, "foo"))
        verified = 1;

    if (!verified)
    {
        printf("Access denied\n");
        exit(1);
    }

    printf("Access granted.\n");

    /* Privileged code follows... */

    return 0;
}