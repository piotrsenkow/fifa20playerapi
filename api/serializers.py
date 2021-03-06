from rest_framework import serializers
from .models import Gk, Cam, Cb, Cdm, Cf, Cm, Lb, Lm, Lw, Lwb, Rb, Rm, Rw, Rwb, St


class GkSerializer(serializers.ModelSerializer):
    """Serializer for Gk model"""

    class Meta:
        model = Gk
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'gk_diving',
            'gk_handling',
            'gk_kicking',
            'gk_reflexes',
            'gk_speed',
            'gk_positioning',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'goalkeeping_diving',
            'goalkeeping_handling',
            'goalkeeping_kicking',
            'goalkeeping_positioning',
            'goalkeeping_reflexes',
            'player_image'
        )


class CamSerializer(serializers.ModelSerializer):
    """Serializer for Cam model"""

    class Meta:
        model = Cam
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class CbSerializer(serializers.ModelSerializer):
    """Serializer for Cb model"""

    class Meta:
        model = Cb
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class CdmSerializer(serializers.ModelSerializer):
    """Serializer for Cdm model"""

    class Meta:
        model = Cdm
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class CfSerializer(serializers.ModelSerializer):
    """Serializer for Cf model"""

    class Meta:
        model = Cf
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class CmSerializer(serializers.ModelSerializer):
    """Serializer for Cm model"""

    class Meta:
        model = Cm
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class LbSerializer(serializers.ModelSerializer):
    """Serializer for Lb model"""

    class Meta:
        model = Lb
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class LmSerializer(serializers.ModelSerializer):
    """Serializer for Lm model"""

    class Meta:
        model = Lm
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class LwSerializer(serializers.ModelSerializer):
    """Serializer for Lw model"""

    class Meta:
        model = Lw
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class LwbSerializer(serializers.ModelSerializer):
    """Serializer for Lwb model"""

    class Meta:
        model = Lwb
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class RbSerializer(serializers.ModelSerializer):
    """Serializer for Rb model"""

    class Meta:
        model = Rb
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class RmSerializer(serializers.ModelSerializer):
    """Serializer for Rm model"""

    class Meta:
        model = Rm
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class RwSerializer(serializers.ModelSerializer):
    """Serializer for Rw model"""

    class Meta:
        model = Rw
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class RwbSerializer(serializers.ModelSerializer):
    """Serializer for Rwb model"""

    class Meta:
        model = Rwb
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )


class StSerializer(serializers.ModelSerializer):
    """Serializer for St model"""

    class Meta:
        model = St
        fields = (
            'sofifa_id',
            'player_url',
            'short_name',
            'long_name',
            'age',
            'dob',
            'height_cm',
            'weight_kg',
            'nationality',
            'club',
            'overall',
            'potential',
            'value_eur',
            'wage_eur',
            'player_positions',
            'preferred_foot',
            'international_reputation',
            'weak_foot',
            'skill_moves',
            'work_rate',
            'body_type',
            'pace',
            'shooting',
            'passing',
            'dribbling',
            'defending',
            'physic',
            'player_traits',
            'attacking_crossing',
            'attacking_finishing',
            'attacking_heading_accuracy',
            'attacking_short_passing',
            'attacking_volleys',
            'skill_dribbling',
            'skill_curve',
            'skill_fk_accuracy',
            'skill_long_passing',
            'skill_ball_control',
            'movement_acceleration',
            'movement_sprint_speed',
            'movement_agility',
            'movement_reactions',
            'movement_balance',
            'power_shot_power',
            'power_jumping',
            'power_stamina',
            'power_strength',
            'power_long_shots',
            'mentality_aggression',
            'mentality_interceptions',
            'mentality_positioning',
            'mentality_vision',
            'mentality_penalties',
            'mentality_composure',
            'defending_marking',
            'defending_standing_tackle',
            'defending_sliding_tackle',
            'player_image'
        )
