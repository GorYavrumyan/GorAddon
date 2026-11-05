"""Gor_Style — создано в Студии дизайна (addon_API)."""

from addon_API import AddonBase


class Addon(AddonBase):
    def on_load(self, api):
        d = api.design
        with d.batch():
            d.preset('glass', clear=False)
            d.palette('#362bee', 'dark', 0.08)
            d.radius(scale=1.4)
            d.font('Comic Sans MS', None)
            d.buttons('pill')
            d.cards(radius=24, glass=False)
            d.covers(radius=16)
            d.shadow("GameCard", blur=26, dy=8)
            d.hover_glow("GameCard", "{{accent}}", 24)
            d.glow("RunGameBtn", "{{accent}}", 16, pulse_ms=2400)
            d.noise(0.05)
            d.animated_gradient(["{{accent}}", "#7a2dff", "#00d4ff"], 14000, 0.14)
            d.particles("stars", 70)
            d.particles("snow", 80)
            d.particles("fireflies", 36, "{{accent_hover}}", 0.8)
            d.vignette(0.5)
            d.grid(44, "{{accent}}", 0.08)
            d.scanlines(3, 0.10)

    def on_unload(self):
        pass   # api.design откатит всё сам
