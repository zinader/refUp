import { useEffect, useState } from 'react';
import Referrals from './assets/referral_positions.json';
import { Modal } from 'react-bootstrap';

const Referals = () => {


    const [isOpen, setOpen] = useState(false)

    const [data, setData] = useState(null)

    const handleClick = () =>{
        setOpen(true)
    }

    const closeModal = () => {
        setOpen(false)
    }

    useEffect((()=>{
        setData(Referrals.Referrals)
    }),
    []
    )

    const renderReferals = () => {
        return(
            data.map((item)=>{
                return(
                    <div className="col-md-4 col-6">
                        <div className='refer-card'>
                            <h2>
                                {item["Name"]}
                            </h2>
                            <p className='company'>
                                {item["Company Name"]} - {item["Position"]}
                            </p>
                            <p className="skills">
                                {item["Skills Required"]}
                            </p>
                            <div className='refer-btn'>
                                <button onClick={()=>handleClick()}>
                                    Ask to Refer
                                </button>
                            </div>
                        </div>
                    </div>
                )
            })
        )
    }

    return(
        <>
            <div className='list'>
                <div className='row'>
                    {data?renderReferals():null}
                </div>

                <Modal show={isOpen} onHide={closeModal}>
                    <Modal.Header closeButton>

                    </Modal.Header>
                    <Modal.Body>
                        <form>
                            <label htmlFor="name">
                                Name:
                            </label>
                            <input id="name" />
                            <label htmlFor="name">
                                Email:
                            </label>
                            <input id="email" />
                            <label>
                                Upload your Resume:
                            </label>
                            <input type="file" />
                        </form>
                    </Modal.Body>
                </Modal>
            </div>
        </>
    )
}

export default Referals