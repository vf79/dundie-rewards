# How to use

## Load data

Having a file 'people.csv' with the following format:

```csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.example.com
Dwight Schrute, Sales, Manager, schrute@dundlermifflin.example.com
Gabe Lewis, Director, Manager, glewis@dundlermifflin.example.com
```

Run `dundie load` command

```py
dundie load people csv
```

## Viewing data

### Viewing all information

```bash
$ dundie show
                                                Dunder Mifflin Report
+------------------------------------------------------------------------------------------------------------------+
| Email                               | Balance | Last_Movement              | Name           | Dept    | Role     |
|-------------------------------------+---------+----------------------------+----------------+---------+----------+
| jim@dumdlermifflin.example.com      | 700     | 2023-07-04T07:41:37.306250 | Jim Halpert    | Sales   | Salesman |
| schrute@dundlermifflin.example.com  | 400     | 2023-07-04T07:41:37.306250 | Dwight Schrute | Sales   | Manager  |
| lewis@dundlermifflin.example.com    | 100     | 2023-07-04T07:42:06.366565 | Gabe Lewis     | C-Level | CEO      |
+------------------------------------------------------------------------------------------------------------------+
```

### Filtering

Available filters are `--dept` and `--email`

```bash
$ dundie show --dept=Sales
                                                Dunder Mifflin Report
+------------------------------------------------------------------------------------------------------------------+
| Email                               | Balance | Last_Movement              | Name           | Dept    | Role     |
|-------------------------------------+---------+----------------------------+----------------+---------+----------+
| jim@dumdlermifflin.example.com      | 700     | 2023-07-04T07:41:37.306250 | Jim Halpert    | Sales   | Salesman |
| schrute@dundlermifflin.example.com  | 400     | 2023-07-04T07:41:37.306250 | Dwight Schrute | Sales   | Manager  |
+------------------------------------------------------------------------------------------------------------------+
```

> **NOTE** passing `--output=file.json` will save a json file with the results.

## Adding points

An admin user can easily add points to any user or dept.

```bash
$ dundie add 150 --email=jim@dumdlermifflin.example.com
                                                Dunder Mifflin Report
+------------------------------------------------------------------------------------------------------------------+
| Email                               | Balance | Last_Movement              | Name           | Dept    | Role     |
|-------------------------------------+---------+----------------------------+----------------+---------+----------+
| jim@dumdlermifflin.example.com      | 700     | 2023-07-05T09:43:37.406250 | Jim Halpert    | Sales   | Salesman |
+------------------------------------------------------------------------------------------------------------------+
```

Available selectors are `--email` and `--dept`
