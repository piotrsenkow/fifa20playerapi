from django.db import models


# Create your models here.


class Gk(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    player_url = models.CharField(db_column='player_url', max_length = 150)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    height_cm = models.IntegerField(db_column='height_cm')
    weight_kg = models.IntegerField(db_column='weight_kg')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    overall = models.IntegerField(db_column='overall')
    potential = models.IntegerField(db_column='potential')
    value_eur = models.IntegerField(db_column='value_eur')
    wage_eur = models.IntegerField(db_column='wage_eur')
    # different length for all other positions
    player_positions = models.CharField(db_column='player_positions', max_length=2)
    preferred_foot = models.CharField(db_column='preferred_foot', max_length=5)
    international_reputation = models.IntegerField(db_column='international_reputation')
    weak_foot = models.CharField(db_column='weak_foot', max_length=5)
    skill_moves = models.IntegerField(db_column='skill_moves')
    work_rate = models.CharField(db_column='work_rate', max_length=30)
    body_type = models.CharField(db_column='body_type', max_length=30)
    gk_diving = models.IntegerField(db_column='gk_diving')
    gk_handling = models.IntegerField(db_column='gk_handling')
    gk_kicking = models.IntegerField(db_column='gk_kicking')
    gk_reflexes = models.IntegerField(db_column='gk_reflexes')
    gk_speed = models.IntegerField(db_column='gk_speed')
    gk_positioning = models.IntegerField(db_column='gk_positioning')
    player_traits = models.CharField(db_column='player_traits', max_length=200)
    attacking_crossing = models.IntegerField(db_column='attacking_crossing')
    attacking_finishing = models.IntegerField(db_column='attacking_finishing')
    attacking_heading_accuracy = models.IntegerField(db_column='attacking_heading_accuracy')
    attacking_short_passing = models.IntegerField(db_column='attacking_short_passing')
    attacking_volleys = models.IntegerField(db_column='attacking_volleys')
    skill_dribbling = models.IntegerField(db_column='skill_dribbling')
    skill_curve = models.IntegerField(db_column='skill_curve')
    skill_fk_accuracy = models.IntegerField(db_column='skill_fk_accuracy')
    skill_long_passing = models.IntegerField(db_column='skill_long_passing')
    skill_ball_control = models.IntegerField(db_column='skill_ball_control')
    movement_acceleration = models.IntegerField(db_column='movement_acceleration')
    movement_sprint_speed = models.IntegerField(db_column='movement_sprint_speed')
    movement_agility = models.IntegerField(db_column='movement_agility')
    movement_reactions = models.IntegerField(db_column='movement_reactions')
    movement_balance = models.IntegerField(db_column='movement_balance')
    power_shot_power = models.IntegerField(db_column='power_shot_power')
    power_jumping = models.IntegerField(db_column='power_jumping')
    power_stamina = models.IntegerField(db_column='power_stamina')
    power_strength = models.IntegerField(db_column='power_strength')
    power_long_shots = models.IntegerField(db_column='power_long_shots')
    mentality_aggression = models.IntegerField(db_column='mentality_aggression')
    mentality_interceptions = models.IntegerField(db_column='mentality_interceptions')
    mentality_positioning = models.IntegerField(db_column='mentality_positioning')
    mentality_vision = models.IntegerField(db_column='mentality_vision')
    mentality_penalties = models.IntegerField(db_column='mentality_penalties')
    mentality_composure = models.IntegerField(db_column='mentality_composure')
    defending_marking = models.IntegerField(db_column='defending_marking')
    defending_standing_tackle = models.IntegerField(db_column='defending_standing_tackle')
    defending_sliding_tackle = models.IntegerField(db_column='defending_sliding_tackle')
    goalkeeping_diving = models.IntegerField(db_column='goalkeeping_diving')
    goalkeeping_handling = models.IntegerField(db_column='goalkeeping_handling')
    goalkeeping_kicking = models.IntegerField(db_column='goalkeeping_kicking')
    goalkeeping_positioning = models.IntegerField(db_column='goalkeeping_positioning')
    goalkeeping_reflexes = models.IntegerField(db_column='goalkeeping_reflexes')
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = False
        db_table = 'gk'

    class Database:
        using = 'fifa'

