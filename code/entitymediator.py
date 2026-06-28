from code.const import NIVEL, SCORE, MENU


class EntityMediator:

    @staticmethod
    def verify(player, enemy):

        if not enemy.alive:
            return SCORE

        if player.rect.colliderect(enemy.rect):

            # Mario caiu sobre o Sonic
            if player.vel_y > 0 and player.rect.bottom < enemy.rect.centery:

                enemy.alive = False

                player.vel_y = -10

                return SCORE

            # Colisão lateral
            return MENU

        return NIVEL