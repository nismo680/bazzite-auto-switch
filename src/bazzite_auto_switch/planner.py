from __future__ import annotations

from dataclasses import dataclass

from bazzite_auto_switch.modes import Mode


@dataclass(slots=True, frozen=True)
class ActionPlan:
    current_mode: Mode | None
    desired_mode: Mode | None

    @property
    def needs_action(self) -> bool:
        return self.current_mode != self.desired_mode


def plan_action(
    current_mode: Mode | None,
    desired_mode: Mode | None,
) -> ActionPlan:
    return ActionPlan(
        current_mode=current_mode,
        desired_mode=desired_mode,
    )
