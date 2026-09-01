import streamlit as st
def render_sidebar():
        
        with st.sidebar:
            st.title("🏋️ AI Gym Trainer")

            st.divider()

            # =========================
            # Workout Plan
            # =========================
            st.subheader("📋 Workout Plan")

            exercise = st.selectbox(
                "Exercise",
                ["Squats", "Bicep Curls", "Push Ups", "Lunges"],
                index=0
            )

            sets = st.number_input(
                "Target Sets",
                min_value=1,
                value=3,
                step=1
            )

            reps = st.number_input(
                "Reps per Set",
                min_value=1,
                value=10,
                step=1
            )

            st.session_state.plan_exercise = exercise
            st.session_state.plan_sets = sets
            st.session_state.plan_reps = reps

            st.divider()

            # =========================
            # Workout Progress
            # =========================
            st.subheader("📊 Workout Progress")

            completed_sets = st.session_state.get("sets_completed", 0)
            current_reps = st.session_state.get("current_set_reps", 0)

            st.metric(
                "Sets Completed",
                f"{completed_sets} / {sets}"
            )

            st.metric(
                "Current Set Reps",
                f"{current_reps} / {reps}"
            )

            # Progress bar
            progress = min(completed_sets / sets, 1.0) if sets > 0 else 0
            st.progress(progress)

            if st.session_state.get("workout_complete", False):
                st.success("🎉 Workout Complete!")

            st.divider()

            # =========================
            # Live Angles
            # =========================
            st.subheader("📐 Live Angles")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Knee",
                    f"{st.session_state.get('knee_angle', 0)}°"
                )

                st.metric(
                    "Elbow",
                    f"{st.session_state.get('elbow_angle', 0)}°"
                )

                st.metric(
                    "Front Knee",
                    f"{st.session_state.get('front_knee_angle', 0)}°"
                )

            with col2:
                st.metric(
                    "Back",
                    f"{st.session_state.get('back_angle', 0)}°"
                )

                st.metric(
                    "Torso",
                    f"{st.session_state.get('torso_angle', 0)}°"
                )

            st.divider()

            # =========================
            # Form Status
            # =========================
            st.subheader("🧍 Form Status")

            status_fields = {
                "Depth": "depth_status",
                "Body Alignment": "body_alignment",
                "Hip": "hip_status",
                "Shoulder": "shoulder_status",
                "Swing": "swing_status",
                "Extension": "extension_status",
                "Back Arch": "back_arch_status",
                "Balance": "balance_status",
            }

            for label, key in status_fields.items():

                status = st.session_state.get(key, "N/A")

                if status in ["Good", "Correct", "OK", "Proper"]:
                    st.success(f"✅ {label}: {status}")

                elif status in ["Bad", "Incorrect", "Poor", "Wrong"]:
                    st.error(f"❌ {label}: {status}")

                elif status in ["Warning", "Adjust", "Too High", "Too Low"]:
                    st.warning(f"⚠️ {label}: {status}")

                else:
                    st.info(f"ℹ️ {label}: {status}")

            st.divider()

            # =========================
            # Workout Controls
            # =========================
            st.subheader("🎮 Controls")

            if not st.session_state.get("workout_started", False):

                if st.button("▶️ Start Workout", use_container_width=True):
                    st.session_state.workout_started = True
                    st.session_state.target_sets = sets
                    st.session_state.reps_per_set = reps
                    st.rerun()

            else:

                if st.button("⏹️ Stop Workout", use_container_width=True):
                    st.session_state.workout_started = False
                    st.rerun()