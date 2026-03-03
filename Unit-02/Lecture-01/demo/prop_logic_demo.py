from __future__ import annotations

import re
from itertools import product
from typing import Dict, Iterable, List, Tuple


def imp(p: bool, q: bool) -> bool:
    """Implication: p -> q is equivalent to (not p) or q."""
    return (not p) or q


def iff(p: bool, q: bool) -> bool:
    """Biconditional: p <-> q."""
    return p == q


_KEYWORDS = {"and", "or", "not", "imp", "iff", "True", "False"}
_NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def extract_symbols(expressions: List[str]) -> List[str]:
    symbols = set()
    for expr in expressions:
        for name in _NAME_RE.findall(expr):
            if name in _KEYWORDS:
                continue
            symbols.add(name)
    return sorted(symbols)


def eval_expr(expr: str, env: Dict[str, bool]) -> bool:
    """
    Evaluate a propositional expression written in Python syntax.

    Allowed:
      - variables: p, q, Rain, GroundWet, ...
      - operators: and, or, not
      - functions: imp(p, q), iff(p, q)

    NOTE: This is intended for trusted classroom input only.
    """
    safe_globals = {"__builtins__": {}, "imp": imp, "iff": iff}
    return bool(eval(expr, safe_globals, dict(env)))


def all_models(symbols: List[str]) -> Iterable[Dict[str, bool]]:
    for values in product([False, True], repeat=len(symbols)):
        yield dict(zip(symbols, values))


def truth_table(expr: str) -> Tuple[List[str], List[Dict[str, bool]]]:
    symbols = extract_symbols([expr])
    rows: List[Dict[str, bool]] = []
    for model in all_models(symbols):
        rows.append({**model, "VALUE": eval_expr(expr, model)})
    return symbols, rows


def entails(kb: List[str], alpha: str) -> Tuple[bool, Dict[str, bool] | None]:
    """
    Returns (entailed, counterexample_model).
    counterexample_model is a model where KB is true but alpha is false.
    """
    symbols = extract_symbols(kb + [alpha])
    for model in all_models(symbols):
        if all(eval_expr(sentence, model) for sentence in kb):
            if not eval_expr(alpha, model):
                return False, model
    return True, None


def fmt_tf(value: bool) -> str:
    return "T" if value else "F"


def print_table(expr: str) -> None:
    symbols, rows = truth_table(expr)
    header = "  ".join([f"{s:>5}" for s in symbols] + [f"{expr:>16}"])
    print(header)
    print("-" * len(header))
    for row in rows:
        vals = [fmt_tf(row[s]) for s in symbols] + [fmt_tf(row["VALUE"])]
        print("  ".join([f"{v:>5}" for v in vals]))


def main() -> None:
    print("\n=== Truth table example ===")
    expr = "(p and q) or (not p)"
    print_table(expr)

    print("\n=== Entailment example (Modus Ponens) ===")
    kb = ["imp(p, q)", "p"]
    alpha = "q"
    ok, counter = entails(kb, alpha)
    print(f"KB = {kb}")
    print(f"alpha = {alpha}")
    print(f"KB |= alpha ?  {ok}")
    if not ok and counter is not None:
        print("Counterexample model (KB true, alpha false):", counter)

    print("\n=== Non-entailment example ===")
    kb2 = ["p"]
    alpha2 = "q"
    ok2, counter2 = entails(kb2, alpha2)
    print(f"KB = {kb2}")
    print(f"alpha = {alpha2}")
    print(f"KB |= alpha ?  {ok2}")
    if not ok2 and counter2 is not None:
        print("Counterexample model:", counter2)


if __name__ == "__main__":
    main()

