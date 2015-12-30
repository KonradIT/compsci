##Logic Gates

Logic gates are symbols to represent a process, that gives an output in HIGH or LOW, like AND. A representation of AND in Java would be 

```
if(a=1); 
	if(b=1); 
		console.log("HIGH")
```

###Truth tables for Logic Gates

####Simple ones

**AND**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |

**OR**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 1      |

**NOT**

| Input A | Input B |
|---------|---------|
| 0       | 1       |

####Advanced ones

**NOR**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 0      |

**NAND**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |



